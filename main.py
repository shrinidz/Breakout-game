from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from lives import Lives
from time import sleep
from score import Score
import random

COLORS = ['CornflowerBlue', 'coral2', 'hotpink', 'LightCyan4', 'seagreen', 'DarkOliveGreen1', 'DarkOrchid']

BLOCK_POSITIONS = [
    (-250, -40), (-250, -10), (-250, 20), (-250, 50), (-250, 80), (-250, 110), (-250, 140), (-250, 170),
    (-200, -40), (-200, -10), (-200, 20), (-200, 50), (-200, 80), (-200, 110), (-200, 140), (-200, 170),
    (-150, -40), (-150, -10), (-150, 20), (-150, 50), (-150, 80), (-150, 110), (-150, 140), (-150, 170),
    (-100, -40), (-100, -10), (-100, 20), (-100, 50), (-100, 80), (-100, 110), (-100, 140), (-100, 170),
    (-50, -40), (-50, -10), (-50, 20), (-50, 50), (-50, 80), (-50, 110), (-50, 140), (-50, 170),
    (0, -40), (0, -10), (0, 20), (0, 50), (0, 80), (0, 110), (0, 140), (0, 170),
    (50, -40), (50, -10), (50, 20), (50, 50), (50, 80), (50, 110), (50, 140), (50, 170),
    (100, -40), (100, -10), (100, 20), (100, 50), (100, 80), (100, 110), (100, 140), (100, 170),
    (150, -40), (150, -10), (150, 20), (150, 50), (150, 80), (150, 110), (150, 140), (150, 170),
    (200, -40), (200, -10), (200, 20), (200, 50), (200, 80), (200, 110), (200, 140), (200, 170),
    (250, -40), (250, -10), (250, 20), (250, 50), (250, 80), (250, 110), (250, 140), (250, 170),
]

BALL_POSITION = (0, -100)

screen = Screen()
screen.title('Breakout')
screen.bgcolor('black')
screen.setup(width=600, height=500)
screen.tracer(0)

paddle = Paddle()
ball = Ball(BALL_POSITION)
lives = Lives()
score = Score()

screen.listen()
screen.onkey(paddle.right, 'Right')
screen.onkey(paddle.left, 'Left')

# Creates Blocks
all_blocks = []

for position in BLOCK_POSITIONS:
    new_block = Turtle('square')
    new_block.penup()
    new_block.color(random.choice(COLORS))
    new_block.shapesize(stretch_wid=1, stretch_len=2)
    new_block.setpos(position)
    all_blocks.append(new_block)

game_on = True
while game_on:
    sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() < -250:
        ball.reposition()
        lives.decrement_lives()

    # Detects if all three lives were used
    if lives.lives == '':
        lives.game_over()
        game_on = False

    # Detects collision with paddle
    if ball.distance(paddle) < 35:
        ball.bounce_y()

    # Detects Collision with blocks
    for block in all_blocks:
        if ball.distance(block) < 20:
            ball.bounce_y()
            block.hideturtle()
            all_blocks.remove(block)
            score.increase_score()

    # Detects collision with top & bottom walls
    if ball.ycor() > 180:
        ball.bounce_y()

    # Detects collision with left & right walls
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

score.goto(0, 0)
score.write(f'Final Score: {score.score}', align='center', font=('Courier', 20, 'bold'))

screen.exitonclick()
