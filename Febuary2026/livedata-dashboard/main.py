from weather import Weather
from currency_converter import Currency_converter
from joke import Joke
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QFrame)
from dotenv import load_dotenv
load_dotenv()

class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.weather = Weather()
        self.currency_converter = Currency_converter()
        self.joke = Joke()
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Live data dashboard")
        vline = QFrame()
        vline.setFrameShape(QFrame.VLine)
        vline.setFrameShadow(QFrame.Sunken)

        hline = QFrame()
        hline.setFrameShape(QFrame.HLine)
        hline.setFrameShadow(QFrame.Sunken)

        self.main_layout = QVBoxLayout()

        hbox = QHBoxLayout()

        hbox.addWidget(self.weather)
        hbox.addWidget(vline)
        hbox.addWidget(self.currency_converter)
        self.main_layout.addLayout(hbox)
        self.main_layout.addWidget(hline)
        self.main_layout.addWidget(self.joke)

        self.setLayout(self.main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = Mainwindow()
    main_app.show()
    sys.exit(app.exec_())

