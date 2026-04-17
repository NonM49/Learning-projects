import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QLineEdit, QGridLayout)

class Calculater(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        
        grid = QGridLayout()

        buttons = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
                   "a", "s", "d", "f", "g", "h", "j", "k", "l", ";",
                   "z", "x", "c", "v", "b", "n", "m", ",", ".", "/",
                   "←"]
        
        row = 0
        col = 0
        for button in buttons:
            btn = QPushButton(button)
            btn.clicked.connect(self.button_clicked)
            if btn.text() == "←":
                grid.addWidget(btn, row, col, row, 3)
            else: grid.addWidget(btn, row, col)

            col += 1
            if col > 9:
                col = 0
                row += 1
        

        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(grid)
        self.setLayout(layout)

    def button_clicked(self):
        button = self.sender()
        text = button.text()


        if text == "←":
            current = self.display.text()
            self.display.setText(current[:-1])

        else: self.display.setText(self.display.text() + text)

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculater = Calculater()
    calculater.show()
    sys.exit(app.exec_())






    


