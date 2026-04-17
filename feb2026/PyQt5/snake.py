import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QGridLayout, QMainWindow)
from PyQt5.QtCore import Qt, QTimer
import random

def change_box_color(board_list, target):
    for row, col in target.pos:
            board_list[row][col].setStyleSheet(f"background-color: {target.color};")

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.snake = Snake()
        self.food = Food()
        self.board_size = 20
        self.board_list = []
        self.direction = "LEFT"
        self.next_direction = "LEFT"
        self.score = 0

        self.game_speed = 200

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game)
        self.timer.start(self.game_speed)

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        self.setWindowTitle("Snake Game")
        self.setGeometry(700, 250, 400, 400)
        self.setFixedSize(self.size())


        self.main_layout = QVBoxLayout()

        self.score_label = QLabel(f"SCORE : {self.score}")
        self.score_label.setStyleSheet("""font-size: 20px;""")
        self.score_label.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("font-weight: bold;")

        self.board = QGridLayout()
        self.board.setSpacing(0)
        #self.board.setContentsMargins(0, 0, 0, 0)

        for row in range(self.board_size):
            row_boxs = []
            for col in range(self.board_size):
                self.box = QLabel()
                self.board.addWidget(self.box, row, col)
                self.box.setStyleSheet("background-color: grey;")
                row_boxs.append(self.box)
            self.board_list.append(row_boxs)

        change_box_color(self.board_list, self.snake)

        #set food
        self.food.draw_food(self.board_list)

        self.main_layout.addWidget(self.score_label)
        self.main_layout.addLayout(self.board)

        self.main_layout.setStretch(0, 0)
        self.main_layout.setStretch(1, 1)

        central_widget.setLayout(self.main_layout)

        self.overlay = QLabel("GAME OVER!\nPress R to restart", self)
        self.overlay.setAlignment(Qt.AlignCenter)

        self.overlay.setStyleSheet("""
            background-color: rgba(0, 0, 0, 180);
            color: white;
            font-size: 24px;
            font-weight: bold;
            border-radius: 10px;
        """)

        self.overlay.hide()

    def keyPressEvent(self, event):  # CALL AUTOMATICLY
        if event.key() == Qt.Key_R:
            self.restart()

        elif event.key() == Qt.Key_Left and self.direction != "RIGHT":
            self.next_direction = "LEFT"

        elif event.key() == Qt.Key_Right and self.direction != "LEFT":
            self.next_direction = "RIGHT"

        elif event.key() == Qt.Key_Up and self.direction != "DOWN":
            self.next_direction = "UP"

        elif event.key() == Qt.Key_Down and self.direction != "UP":
            self.next_direction = "DOWN"

    def resizeEvent(self, event): #let overlay stay center of the window
        super().resizeEvent(event)

        w = 250
        h = 125

        cw = self.centralWidget()

        x = (cw.width() - w) // 2 #center fomular
        y = (cw.height() - h) // 2

        self.overlay.setGeometry(x, y, w, h)

    def update_game(self):

        self.direction = self.next_direction

        row, col = self.snake.head
         
        if self.direction == "LEFT":
            self.snake.head = (row, col - 1)
        elif self.direction == "RIGHT":
            self.snake.head = (row, col + 1)
        elif self.direction == "UP":
            self.snake.head = (row - 1, col)
        elif self.direction == "DOWN":
            self.snake.head = (row + 1, col)
        else:
            self.snake.head = (row, col - 1)

        rows = self.board_size
        cols = self.board_size

        row, col = self.snake.head

        if row < 0 or row >= rows or col < 0 or col >= cols:
            self.game_over()
            return
            
        if self.snake.head in self.snake.pos[:-1]:
            self.game_over()
            return
        
        if self.food.pos == self.snake.head:
            self.snake_ate = True

            while True:
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - 1)

                if (row, col) not in self.snake.pos:
                    self.food.pos = (row, col)
                    break

            self.score += 1
            self.score_label.setText(f"SCORE : {self.score}")
            self.food.draw_food(self.board_list)

        else:
            self.snake_ate = False
        

        if not self.snake_ate:
            tail = self.snake.pos.pop(0)

            row, col = tail
            self.board_list[row][col].setStyleSheet("background-color: grey;")

        self.snake.pos.append(self.snake.head)
        change_box_color(self.board_list, self.snake)

    def restart(self):
        self.overlay.hide()

        self.snake = Snake()
        self.food = Food()
        self.direction = "LEFT"
        self.next_direction = "LEFT"
        self.score = 0
        self.score_label.setText(f"SCORE : {self.score}")

        #reset board color 
        for row in self.board_list:
            for box in row:
                box.setStyleSheet("background-color: grey;")

        change_box_color(self.board_list, self.snake)
        self.food.draw_food(self.board_list)

        self.timer.start(self.game_speed)

    def game_over(self):
        self.timer.stop()
        self.overlay.show()


class Snake():
    def __init__(self):
        self.pos = [(10, 14), (10, 13)]
        self.color = "green"
        self.head = self.pos[-1]

class Food():
    def __init__(self):
        self.pos = (10, 7)
        self.color = "red"

    def draw_food(self, target):
        row, col = self.pos
        target[row][col].setStyleSheet(f"background-color: {self.color};")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())


#what I learn
#.pop()
#you dont need to manual call the keypressevent medthod
#snake.pos[:-1]  (not include the last item in a list)
#known how .self work