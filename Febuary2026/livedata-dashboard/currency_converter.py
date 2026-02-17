import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt, QTimer
from utils import get_http_error_message
import os

class Currency_converter(QWidget):
    def __init__(self):
        super().__init__()
        self.main_label = QLabel("CURRENCY CONVERTER 💲\nTHB → USD")
        self.thb_input_amount = QLineEdit()
        self.usd_respon_amount_text = QLineEdit()
        self.exchange_button = QPushButton("convert")
        self.active_label = QLabel()
        self.timer = QTimer()
        self.timer.setSingleShot(True) 

        self.initUI()

    def initUI(self):

        self.setFixedSize(200, 200)
        
        self.thb_symbol = QLabel("฿")
        self.usd_symbol = QLabel("$")

        self.thb_input_amount.setPlaceholderText("Enter THB")


        self.main_label.setStyleSheet("""font-size: 12px;
                                      font-weight: bold;""")
        self.main_layout = QVBoxLayout()

        self.boxs_layout = QHBoxLayout()
        self.boxs_layout.addWidget(self.thb_symbol)
        self.boxs_layout.addWidget(self.thb_input_amount)
        self.boxs_layout.addWidget(self.usd_symbol)
        self.boxs_layout.addWidget(self.usd_respon_amount_text)
        self.usd_respon_amount_text.setReadOnly(True)

        self.main_layout.addWidget(self.main_label)
        self.main_label.setAlignment(Qt.AlignCenter)

        self.main_layout.addLayout(self.boxs_layout)
        self.main_layout.addWidget(self.exchange_button)

        self.main_layout.addWidget(self.active_label)
        self.active_label.setAlignment(Qt.AlignCenter)

        self.setLayout(self.main_layout)
        self.exchange_button.clicked.connect(self.convert)
        

    def convert(self):
        self.active_label.setText("")
        api_key = os.getenv("CURRENCY_API_KEY")
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            thb_rate = data["conversion_rates"]["THB"]
            rate = 1 / thb_rate

            raw_thb_amount = self.thb_input_amount.text().replace(",", "")
            thb_amount = float(raw_thb_amount)
            usd_amount = thb_amount * rate

            self.trigger_active_label("Converted!", "black")
            QTimer.singleShot(1000, lambda: self.thb_input_amount.setText(f"{thb_amount:,}"))
            QTimer.singleShot(1000, lambda: self.usd_respon_amount_text.setText(f"{usd_amount:,.2f}"))

        except ValueError:
            self.trigger_active_label("Please Enter numbers Only.")

        except requests.exceptions.HTTPError as http_error:
            self.trigger_active_label(get_http_error_message(response, http_error))

        except requests.exceptions.ConnectionError:
            self.trigger_active_label("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.trigger_active_label("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.trigger_active_label("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.trigger_active_label(f"Request Error:\n{req_error}")

    def trigger_active_label(self, message, color = "red"):
        self.active_label.setStyleSheet("")
        self.active_label.setText("...")

        self.timer.stop()
        try:
            self.timer.timeout.disconnect()
        except:
            pass
        self.timer.timeout.connect(lambda: self.display_active_label(message, color))
        self.timer.start(1000)

    def display_active_label(self, message, color = "red"):
        self.active_label.setStyleSheet(f"color: {color};")
        self.active_label.setText(message)

