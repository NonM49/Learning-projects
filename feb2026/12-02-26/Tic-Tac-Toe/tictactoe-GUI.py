import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QGridLayout, QMainWindow)
from PyQt5.QtCore import Qt



class Main_board(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.board = [" "] * 9
        self.setGeometry(700, 250, 400, 400)
        self.turn = 0
        self.initUI()
        self.setFixedSize(self.size())


    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout()

        self.check_turn()

        self.main_label = QLabel("")
        self.main_label.setText(f"{self.player}'s Turn")

        self.main_label_style()
        self.main_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.main_label)

        self.button_layout = QHBoxLayout()
        self.main_layout.addLayout(self.button_layout)

        self.ask_restart = QPushButton("Restart")
        self.ask_quit = QPushButton("Quit")
        self.button_layout.addWidget(self.ask_restart)
        self.button_layout.addWidget(self.ask_quit)

        self.grid = QGridLayout()
        self.main_layout.addLayout(self.grid)

        central_widget.setLayout(self.main_layout)

        self.ask_restart.hide()
        self.ask_quit.hide()

        self.buttons = []

        for row in range(3):
            for col in range(3):
                btn = QPushButton("")
                btn.setFixedSize(100, 100)
                btn.setStyleSheet("font-size: 80px;"
                                  "color: black")

                index = row * 3 + col

                self.grid.addWidget(btn, row, col)
                self.buttons.append(btn)
                btn.clicked.connect(lambda _, i=index: self.on_click(i))

    def on_click(self, index):

        self.board[index] = self.player

        btn = self.buttons[index]
        btn.setText(self.player)
        btn.setEnabled(False)


        if self.check_win(self.player):
            self.game_over(f"{self.player} wins!")
            return
        elif self.turn >= 8:
            self.game_over("Draw!")
            return

        self.turn += 1
        self.check_turn()
        self.main_label_style()
        self.main_label.setText(f"{self.player}'s Turn")

    def check_win(self, player):
        wins = [(0, 1, 2),
                (3, 4, 5),
                (6, 7, 8),
                (0, 3, 6),
                (1, 4, 7),
                (2, 5, 8),
                (0, 4, 8),
                (2, 4, 6)]
        
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] == player:
                return True
        return False

    def game_over(self, message):
        for btn in self.buttons:
            btn.setEnabled(False)

        self.main_label.setText(f"GAME OVER\n{message}")
        self.main_label.setStyleSheet("""
                                    font-weight: bold;
                                    color: red;
                                 """)

        self.ask_restart.show()
        self.ask_quit.show()
        

        self.ask_restart.clicked.connect(self.restart_game)
        self.ask_quit.clicked.connect(self.quit_game)

    def restart_game(self):
        self.board = [" "] * 9
        self.turn = 0
        self.check_turn()
        self.main_label_style()
        self.main_label.setText(f"{self.player}'s Turn")

        for btn in self.buttons:
            btn.setText("")
            btn.setEnabled(True)

        self.ask_restart.hide()
        self.ask_quit.hide()

    def quit_game(self):
        quit()

    def check_turn(self):
        if self.turn % 2 == 0:
            self.player = "X"
        else:
            self.player = "O"

    def main_label_style(self):
        self.main_label.setStyleSheet("font-size: 20px;"
                                      "font-weight: bold;"
                                      "color: black;")
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_board = Main_board()
    main_board.show()
    sys.exit(app.exec_())
