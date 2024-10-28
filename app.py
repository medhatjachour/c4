import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QFileDialog , QLabel
from PySide6.QtGui import QFont,QIcon

from main import Ui_MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        # selected file 
        self.file = None
        self.ui.browse_file.clicked.connect(self.showDialog)
        self.ui.delete_2.clicked.connect(self.delete_file)
        self.ui.scrape.clicked.connect(self.showData)
        self.ui.delete_2.hide()     
        self.ui.scrape.hide() 
        self.ui.frame_2.hide()    
        # Set the window title
        self.setWindowTitle("My Application Title")
        # Set the window icon
        # self.setWindowIcon(QIcon('path/to/icon.png'))
        self.font = QFont("Proxima Nova",10)    
        self.data = ["aborder border-slate-700 ...border border-slate-700 ...border border-slate-700 ...border border-slate-700 ...border border-slate-700 ...border border-slate-700 ...border border-slate-700 ...border border-slate-700 ...border border-slate-700 ...border border-slate-700 ...","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    def showDialog(self): # here a funcion to choose the file  
        if self.file:
            self.ui.error.setText("You can't choose more than one file ")
        else:
            self.fileName = QFileDialog.getOpenFileName(self, "Chose media", "/","Media Files (*)")
            self.file = self.fileName[0]
            if self.file:
                self.ui.label_file.setText(self.file)
                self.ui.delete_2.show() 
                self.ui.scrape.show()
                self.ui.frame_2.show()    
    # delete function add ur logic here 
    def delete_file(self):
        self.file = None
        self.ui.label_file.setText("")
        self.ui.delete_2.hide()       
        self.ui.scrape.hide()   
        self.ui.frame_2.hide()    
    # here a function to add the data 
    def showData(self):
        self.ui.frame.hide()
        self.ui.frame_2.hide()
        for i in self.data:
            self.addLabel = QLabel()
            self.addLabel.setFont(self.font)
            self.addLabel.setMinimumHeight(35)
            self.ui.verticalLayout_13.addWidget(self.addLabel)
            self.addLabel.setText(i)
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())