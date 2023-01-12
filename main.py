import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt App")
        label = QLabel(self)
        label.setText("Siema")
        label.setStyleSheet("color:red; font-size:15px")
        checkbox = QCheckBox(self)
        self.sendMessage()
    def sendMessage(self):
        QMessageBox.information(self,"Notify","Hello world!")


if __name__=='__main__':
    app = QApplication([])
    main = Main()
    main.show()

    sys.exit(app.exec_())