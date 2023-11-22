from turtle import Turtle


class Lives(Turtle):

    def __init__(self):
        super().__init__()
        self.lives = '❤️❤️❤️'
        self.color('LightBlue')
        self.penup()
        self.setpos(200, 210)
        self.update_lives()
        self.hideturtle()

    def update_lives(self):
        self.write(f'lives:  {self.lives}', align='center', font=('Cursive', 12, 'bold'))

    def decrement_lives(self):
        try:
            if self.lives == '❤️❤️❤️':
                self.lives = self.lives.replace('❤️❤️❤️', '❤️❤️')

            elif self.lives == '❤️❤️':
                self.lives = self.lives.replace('❤️❤️', '❤️')

            elif self.lives == '❤️':
                self.lives = self.lives.replace('❤️', '')

        finally:
            self.clear()
            self.update_lives()

    def game_over(self):
        self.goto(-50, 210)
        self.write('GAME OVER!', align="left", font=('Cursive', 8, 'bold'))


