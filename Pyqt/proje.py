import sys 
from PyQt6.QtWidgets import *
from ui_form import Ui_MainWindow

class Anaform(Ui_MainWindow,QMainWindow):
          def __init__(self) :
                  super().__init__()
                  self.setupUi(self)
                  self.show() 
                  self.pushButton.clicked.connect(self.ekle)
                  self.pushButton_2.clicked.connect(self.sil)
                    
          def ekle(self):
                  x= self.lineEdit.text()
                  self.listWidget.addItem(x)
                  self.comboBox.addItem(x)
                  self.checkBox.setText(x)
                  self.checkBox_2.setText(x)
                  self.checkBox_3.setText(x)



          def sil (self):
                  self.listWidget.clear()  
                  self.comboBox.clear()
                  self.checkBox.setText("")
                  self.checkBox_2.setText("")
                  self.checkBox_3.setText("")


                                
                  

proje = QApplication(sys.argv)
form1 = Anaform()
form1.show()
sys.exit(proje.exec())                  