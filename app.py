import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PySide6.QtGui import QFont, QIcon

from main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.add_label = None
        self.file_name = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # Selected file
        self.file = None
        self.ui.browse_file.clicked.connect(self.show_dialog)
        self.ui.delete_2.clicked.connect(self.delete_file)
        self.ui.scrape.clicked.connect(self.show_data)
        self.ui.delete_2.hide()
        self.ui.scrape.hide()
        self.ui.frame_2.hide()
        # Set the window title
        self.setWindowTitle("C411")
        # Set the window icon
        self.setWindowIcon(QIcon('icons/app.ico'))
        self.font = QFont("Proxima Nova", 10)

    # Here a function to choose the file
    def show_dialog(self):
        if self.file:
            self.ui.error.setText("You can't choose more than one file ")
        else:
            self.file_name = QFileDialog.getOpenFileName(
                self,
                "Choose Spreadsheet",
                "/",
                "Spreadsheet Files (*.xlsx *.xls *.gsheet *.ods);;Excel Files (*.xlsx *.xls);;Google Sheets ("
                "*.gsheet);;LibreOffice Sheets (*.ods)"
            )
            self.file = self.file_name[0]
            if self.file:
                self.ui.label_file.setText(self.file)
                self.ui.delete_2.show()
                self.ui.scrape.show()
                self.ui.frame_2.show()

    # Delete function add logic here
    def delete_file(self):
        self.file = None
        self.ui.label_file.setText("")
        self.ui.delete_2.hide()
        self.ui.scrape.hide()
        self.ui.frame_2.hide()

    # Here a function to add the data
    def show_data(self, data):
        self.ui.frame.hide()
        self.ui.frame_2.hide()
        self.add_label = QLabel()
        self.add_label.setFont(self.font)
        self.add_label.setMinimumHeight(25)
        self.ui.verticalLayout_13.addWidget(self.add_label)
        self.add_label.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.show_data('First try')
    sys.exit(app.exec())
