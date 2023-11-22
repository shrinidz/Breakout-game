from turtle import Turtle

POSITION = (0, -200)


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('#D0D4CA')
        self.shapesize(stretch_wid=0.5, stretch_len=6)
        self.speed('fastest')
        self.setpos(POSITION)

    def right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

