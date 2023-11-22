'''SCORE.PY'''

from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-50, 220)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align='right', font=('Courier', 16, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()
