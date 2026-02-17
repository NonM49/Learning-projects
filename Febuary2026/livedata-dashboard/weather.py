import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QLineEdit, QVBoxLayout)
from PyQt5.QtCore import Qt
from utils import get_http_error_message
import os

class Weather(QWidget):
    def __init__(self):
        super().__init__()
        self.main_label = QLabel("WEATHER ⛅", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("get weather", self)
        self.temperature_label = QLabel("Enter a city.", self)
        self.weather_emoji_label = QLabel(self)
        self.weather_label = QLabel(self)
        self.initUI()

    def initUI(self):

        self.setFixedSize(200, 200)
        self.city_input.setPlaceholderText("Enter a city")
        
        vbox = QVBoxLayout()

        vbox.addWidget(self.main_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.weather_emoji_label)
        vbox.addWidget(self.weather_label)

        self.main_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.weather_emoji_label.setAlignment(Qt.AlignCenter)
        self.weather_label.setAlignment(Qt.AlignCenter)

        self.setLayout(vbox)

        self.main_label.setObjectName("main_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.weather_emoji_label.setObjectName("weather_emoji_label")
        self.weather_label.setObjectName("weather_label")

        self.setStyleSheet("""
                           QLabel{
                           font-size: 15px;
                           }
                           QLabel#main_label{
                           font-size: 15px;
                           font-weight: bold;
                           }
                           QLabel#weather_emoji_label{
                           font-size: 40px;
                           font-family: segoe UI emoji;
                           }
                           """)
        self.get_weather_button.clicked.connect(self.get_weather)
        
    def get_weather(self):
        api_key = os.getenv("WEATHER_API_KEY")
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            self.display_error(get_http_error_message(response, http_error))
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("color: red")
        self.temperature_label.setText(message)
        self.weather_emoji_label.clear()
        self.weather_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        #temperature_f = (temperature_k * 9/5) - 459.67
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        self.weather_emoji_label.setText(self.get_weather_emoji(weather_id))
        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.weather_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "☀"
        elif 800 <= weather_id <= 804:
            return "☁"
        else:
            return ""