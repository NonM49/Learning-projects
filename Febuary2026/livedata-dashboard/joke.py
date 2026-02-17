import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QLineEdit, QVBoxLayout,
                             QGridLayout, QHBoxLayout)
from PyQt5.QtCore import Qt, QTimer

class Joke(QWidget):
    def __init__(self):
        super().__init__()
        self.main_label = QLabel("RANDOM JOKE 😂")
        self.generate_joke_button = QPushButton("Click!")
        self.display_joke = QLabel()
        self.initUI()

    def initUI(self):

        self.setFixedSize(400, 300)

        self.generate_joke_button.setObjectName("generate_joke_button")
        
        self.setStyleSheet("""QPushButton{
                           font-size: 16px;
                                                padding: 8px 20px;
                                                border: 2.5px solid;
                                                border-radius: 20px;
                           }
                           QPushButton#generate_joke_button:hover{
                           background-color: #b3bcc9;
                           }""")

        self.main_label.setStyleSheet("font-size: 15px;font-weight: bold")
        self.main_label.setAlignment(Qt.AlignCenter)

        self.generate_joke_button.setMaximumWidth(250)

        self.display_joke.setStyleSheet("""font-size: 15px;
                                        color: blue;
                                        background-color: #96b9f2;
                                        margin: 10px;
                                        border: 5px solid;
                                        border-radius: 20px; """)
        self.display_joke.setAlignment(Qt.AlignCenter)
        self.display_joke.setWordWrap(True)

        self.main_layout = QVBoxLayout()

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.generate_joke_button)

        self.main_layout.addWidget(self.main_label, 1)
        self.main_layout.addLayout(self.button_layout, 1)
        self.main_layout.addWidget(self.display_joke, 8)

        self.setLayout(self.main_layout)

        self.generate_joke_button.clicked.connect(self.trigger_joke_generate)

    def trigger_joke_generate(self):
        self.generate_joke_button.setEnabled(False)
        self.display_joke.clear()

        url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw&type=twopart"

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        joke_setup = data["setup"]
        joke_delivery = data["delivery"]
        self.display_joke.setText(joke_setup + "\n\n...")
        QTimer.singleShot(2000, lambda: self.display_joke.setText(joke_setup + "\n\n" + joke_delivery))
        QTimer.singleShot(2000, lambda: self.generate_joke_button.setEnabled(True))

