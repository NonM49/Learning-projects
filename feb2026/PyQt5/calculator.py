import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, 
                             QPushButton, QVBoxLayout,
                             QLineEdit, QGridLayout)

class Calculater(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")
        #self.setGeometry(700, 300, 400, 500)

        self.display = QLineEdit()
        self.display.setReadOnly(True)

        grid = QGridLayout()

        buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "0",".","=","+"
        ]

        row = 0
        col = 0

        for button in buttons:
            btn = QPushButton(button)
            btn.clicked.connect(self.on_button_clicked)
            grid.addWidget(btn, row, col)

            col += 1
            if col > 3:
                col = 0
                row += 1

        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(grid)
        self.setLayout(layout)

    def on_button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            try:
                    result = str(eval(self.display.text()))
                    self.display.setText(result)
            except:
                    self.display.setText("Error")
        else:
                self.display.setText(self.display.text() + text)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculater = Calculater()
    calculater.show()
    sys.exit(app.exec_())






    


