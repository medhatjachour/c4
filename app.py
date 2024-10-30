import sys
import os
import asyncio
import timeit
from typing import Optional
from pathlib import Path

from functools import partial
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QLabel,
    QMessageBox
)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Signal, QObject, Slot, QThread

from main import Ui_MainWindow
from yellow_pages import update_sheet
from fileName import Ui_Form


class UpdateWorker(QObject):
    progress = Signal(str)  # Signal for progress updates
    finished = Signal(float)  # Signal for completion with elapsed time
    error = Signal(str)  # Signal for error handling

    def __init__(self, file_path: str, parent=None):
        super().__init__(parent)
        self.file_path = file_path
        self._is_running = True

    def stop(self):
        self._is_running = False

    async def _show_data_async(self, data: str):
        """Thread-safe way to emit progress updates."""
        if self._is_running:
            self.progress.emit(data)

    async def run_update(self):
        """Runs the update process in the background thread."""
        start = timeit.default_timer()

        try:
            await update_sheet(self.file_path, self._show_data_async)
        except Exception as e:
            self.error.emit(f"Error during update: {str(e)}")
            return

        if self._is_running:
            end = timeit.default_timer()
            self.finished.emit(end - start)

    def run(self):
        """Main entry point for the worker thread."""
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.run_update())
            loop.close()
        except Exception as e:
            self.error.emit(f"Critical error in worker thread: {str(e)}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.labelFileName = None
        self.font = None
        self.add_label = None
        self.files_names = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.files: Optional[str] = None
        self.worker: Optional[UpdateWorker] = None
        self.worker_thread: Optional[QThread] = None

        # UI Setup
        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        self.ui.scrape.hide()
        self.ui.frame_2.hide()

        self.setWindowTitle("Yellow Pages")
        self.setWindowIcon(QIcon('icons/app.ico'))
        self.font = QFont("Proxima Nova", 10)

    def setup_connections(self):
        """Setup signal/slot connections."""
        self.ui.browse_file.clicked.connect(self.show_dialog)
        self.ui.scrape.clicked.connect(self.scrape_function)

    def show_dialog(self):
        self.files_names = QFileDialog.getOpenFileNames(
            self,
            "Choose Spreadsheet",
            str(Path.cwd()),  # Start in user's current working directory
            "Spreadsheet Files (*.xlsx *.xls *.gsheet *.ods)"
        )

        self.files = self.files_names[0]
        print("All files before deletion", self.files)
        for i in self.files:
            file = os.path.basename(i)
            self.labelFileName = Ui_Form(file)
            self.ui.verticalLayout_14.addWidget(self.labelFileName)
            self.labelFileName.delete_2.clicked.connect(
                partial(
                    self.delete_from_main, i
                ))
        if self.files:
            self.ui.scrape.show()
            self.ui.frame_2.show()
            self.ui.frame_3.show()

    def delete_from_main(self, i):
        self.files.remove(i)

        if len(self.files) == 0:
            self.ui.frame_3.hide()
            self.ui.scrape.hide()
            self.ui.frame_2.hide()
        print(self.files)

    def delete_file(self):
        self.stop_worker()
        self.files = None
        self.ui.scrape.hide()
        self.ui.frame_2.hide()

    def stop_worker(self):
        """Safely stop the worker thread."""
        if self.worker:
            self.worker.stop()
        if self.worker_thread and self.worker_thread.isRunning():
            self.worker_thread.quit()
            self.worker_thread.wait()
            self.worker = None
            self.worker_thread = None

    def scrape_function(self):
        """Initialize and start the scraping process."""

        self.ui.frame.hide()
        self.ui.frame_3.hide()
        self.ui.frame_2.hide()
        self.ui.scrape.setEnabled(False)

        # Create and setup worker
        self.worker = UpdateWorker(self.files, self)
        self.worker_thread = QThread(self)
        self.worker.moveToThread(self.worker_thread)

        # Connect signals
        self.worker_thread.started.connect(self.worker.run)
        self.worker.progress.connect(self.show_data)
        self.worker.finished.connect(lambda time: self.on_scrape_complete(time))
        self.worker.error.connect(self.handle_error)

        # Start the thread
        self.worker_thread.start()

    @Slot(str)
    def handle_error(self, error_message: str):
        """Handle errors from the worker thread."""
        QMessageBox.critical(self, "Error", error_message)
        self.stop_worker()
        self.ui.scrape.setEnabled(True)

    def on_scrape_complete(self, exe_time: float):
        """Handle completion of the scraping process."""
        hours = exe_time // 3600
        minutes = (exe_time % 3600) // 60
        seconds = (exe_time % 3600) % 60

        elapsed_time = (
            f"\nProcess completed successfully!\n"
            f"Total time: {int(hours)} hours, {int(minutes)} minutes, {round(seconds, 2)} seconds.\n"
        )
        self.show_data(elapsed_time)

        # Clean up
        self.stop_worker()
        self.ui.scrape.setEnabled(True)

    @Slot(str)
    def show_data(self, data: str):
        self.add_label = QLabel()
        self.add_label.setFont(self.font)
        self.add_label.setMinimumHeight(25)
        self.ui.verticalLayout_13.addWidget(self.add_label)
        self.add_label.setText(data)

    def closeEvent(self, event):
        self.stop_worker()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
