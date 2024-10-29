import asyncio
import aiohttp
import requests
from async_timeout import timeout
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl
import random
import time
import pandas as pd
import openpyxl
import os
import re
import json


async def fetch(session, url, old=False):
    try:
        if old:
            lis = ["Mozilla/5.0 (X11; Linux x86_64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                   "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                   "CriOS/114.0.5735.99 Mobile/15E148 Safari/604.1", "Mozilla/5.0 (Linux; Android 10) "
                                                                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                                                                     "Chrome/114.0.5735.57 Mobile Safari/537.36",
                   "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/114.0.5735.57 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; LM-Q720) "
                                                                "AppleWebKit/537.36 (KHTML, like Gecko) "
                                                                "Chrome/114.0.5735.57 Mobile Safari/537.36"]
            agent = random.choice(lis)
        else:
            agent = UserAgent().random
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Accept-Language': 'en-US,en;q=0.5',
                   'Referer': 'https://www.google.ca/',
                   'User-Agent': agent}

        sslcontext = ssl.create_default_context()
        sslcontext.check_hostname = False
        sslcontext.verify_mode = ssl.CERT_NONE
        async with timeout(15):
            async with session.get(url, headers=headers, ssl=sslcontext) as response:
                return await response.text()
    except (aiohttp.ClientError, asyncio.TimeoutError) as e:
        print(f'Error fetching {url}: {e}')
        return None


async def get_new_data(response, show_data):
    try:
        soup = BeautifulSoup(response, 'html.parser')
        name = soup.find('h1', class_='vcard__name')
        if name is None:
            return '', ''

        name = name.text
        address = soup.find('div', class_='c411Address vcard__address').text

        return name, address

    except (AttributeError, TypeError) as e:
        show_data(f'Error parsing new data urls: {e}')


async def update_sheet(file_path, show_data) -> None:
    # Load the spreadsheet
    df = pd.read_excel(file_path)

    # Add Name2 and Address2 columns with empty values
    df['Name2'] = None
    df['Address2'] = None

    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=random.randint(25, 50))) as session:
            for index, row in df.iterrows():
                try:
                    lead_url = f"https://www.canada411.ca/search/?pnum={row['Phone']}"
                    response = await fetch(session, lead_url)
                    name2, address2 = await get_new_data(response, show_data)

                    # Assign values to the new columns
                    df.at[index, 'Name2'] = name2
                    df.at[index, 'Address2'] = address2

                    show_data(
                        f'Updated row {index + 1} for this phone number({row["Phone"]}):'
                        f'\nName2: {name2}, Address2: {address2}')

                    # Non-blocking delay
                    delay = random.randint(1, 3)
                    await asyncio.sleep(delay)

                except Exception as row_error:
                    show_data(f"Error processing row {index}: {row_error}")

    except Exception as e:
        show_data(f'Error with client session: {e}')

    # Save the updated spreadsheet with cleanup
    directory, original_filename = os.path.split(file_path)
    new_filename = f"Updated_{original_filename}"
    new_file_path = os.path.join(directory, new_filename)

    try:
        df.to_excel(new_file_path, index=False)
    except Exception as save_error:
        show_data(f"Error saving file: {save_error}")
    finally:
        del df  # Explicitly remove the DataFrame from memory
