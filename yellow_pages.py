import asyncio
import aiohttp
import ssl
import random
import pandas as pd
import os
from typing import Callable, Coroutine, Any
from async_timeout import timeout
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class YellowPagesError(Exception):
    """Custom exception for Yellow Pages specific errors."""
    pass


async def fetch(session: aiohttp.ClientSession, url: str, old: bool = False) -> str:
    try:
        if old:
            agents = [
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                "CriOS/114.0.5735.99 Mobile/15E148 Safari/604.1",
                "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.57 Mobile "
                "Safari/537.36",
                "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/114.0.5735.57 Mobile Safari/537.36",
                "Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.57 "
                "Mobile Safari/537.36"
            ]
            agent = random.choice(agents)
        else:
            agent = UserAgent().random

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.google.ca/',
            'User-Agent': agent
        }

        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        async with timeout(15):
            async with session.get(url, headers=headers, ssl=ssl_context) as response:
                if response.status != 200:
                    raise YellowPagesError(f"HTTP {response.status}: {response.reason}")
                return await response.text()

    except asyncio.TimeoutError:
        raise YellowPagesError(f"Timeout while fetching {url}")
    except aiohttp.ClientError as e:
        raise YellowPagesError(f"Network error while fetching {url}: {str(e)}")
    except Exception as e:
        raise YellowPagesError(f"Unexpected error while fetching {url}: {str(e)}")


async def get_new_data(response: str) -> tuple[str, str]:
    try:
        soup = BeautifulSoup(response, 'html.parser')

        name_elem = soup.find('h1', class_='vcard__name')
        if not name_elem:
            return '', ''

        address_elem = soup.find('div', class_='c411Address vcard__address')
        if not address_elem:
            return name_elem.text.strip(), ''

        return name_elem.text.strip(), address_elem.text.strip()

    except Exception as e:
        raise YellowPagesError(f"Error parsing response: {str(e)}")


async def update_sheet(
        file_path: str,
        progress_callback: Callable[[str], Coroutine[Any, Any, None]]
) -> None:
    try:
        # Load the spreadsheet
        df = pd.read_excel(file_path)
        if 'Phone' not in df.columns:
            raise YellowPagesError("Spreadsheet must contain a 'Phone' column")

        # Add new columns
        df['Name2'] = None
        df['Address2'] = None

        # Configure client session
        conn = aiohttp.TCPConnector(limit=random.randint(25, 50))
        timeout_config = aiohttp.ClientTimeout(total=30)

        async with aiohttp.ClientSession(connector=conn, timeout=timeout_config) as session:
            for index, row in df.iterrows():
                try:
                    # Skip if no phone number
                    if pd.isna(row['Phone']):
                        await progress_callback(f'Skipping row {index + 1}: No phone number')
                        continue

                    # Fetch and parse data
                    url = f"https://www.canada411.ca/search/?pnum={row['Phone']}"
                    response = await fetch(session, url)
                    name2, address2 = await get_new_data(response)

                    # Update dataframe
                    df.at[index, 'Name2'] = name2
                    df.at[index, 'Address2'] = address2

                    await progress_callback(
                        f'Updated row {index + 1} for {row["Phone"]}:\n'
                        f'Name2: {name2}\nAddress2: {address2}'
                    )

                    # Random delay
                    await asyncio.sleep(random.uniform(1, 2))

                except YellowPagesError as e:
                    await progress_callback(f"Error processing row {index + 1}: {str(e)}")
                except Exception as e:
                    await progress_callback(f"Unexpected error in row {index + 1}: {str(e)}")

        # Save updated file
        directory = os.path.dirname(file_path)
        filename = os.path.basename(file_path)
        new_path = os.path.join(directory, f"Updated_{filename}")

        df.to_excel(new_path, index=False)
        await progress_callback(f"Saved updated data to: {new_path}")

    except Exception as e:
        raise YellowPagesError(f"Failed to update spreadsheet: {str(e)}")
    finally:
        # Cleanup
        if 'df' in locals():
            del df
