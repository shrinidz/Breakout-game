from turtle import Turtle


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('MediumBlue')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.move_speed = 0.1
        self.speed(self.move_speed)
        self.x_move = 10
        self.y_move = 10
        self.setpos(position)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        self.speed(self.move_speed)

    def bounce_y(self):
        self.y_move *= -1

    def reposition(self):
        self.goto(0, -100)
        self.move_speed = 0.1
        self.speed(self.move_speed)
        self.bounce_y()
