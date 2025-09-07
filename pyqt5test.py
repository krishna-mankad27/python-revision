#trying pyqt5 library
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt
class mainwindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("hello world")
        self.setGeometry(0,0,500,500)
        self.setWindowIcon(QIcon("image.png"))
        label = QLabel("hello, how are you",self)
        label.setGeometry(0,0,300,300)
        label.setStyleSheet("color: #fc03e8;""background-color: #c3f7ca;""font-style : italic;""font-weight : bold;""text-decoration : underline;")
        label.setFont(QFont("Arial",10))
        label.setAlignment(Qt.AlignTop)
        label.setAlignment(Qt.AlignHCenter)
        pixmap = QPixmap("intel.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
#        label.setAlignment(Qt.AlignBottom)
def main():
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()

