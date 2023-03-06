from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, create_middle_line
import time

# Screen
screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# Paddles
paddle_r = Paddle()
paddle_r.setposition(x=350, y=0)
screen.onkeypress(paddle_r.move_up, "Up")
screen.onkeypress(paddle_r.move_down, "Down")

paddle_l = Paddle()
paddle_l.setposition(x=-350, y=0)
screen.onkeypress(paddle_l.move_up, "w")
screen.onkeypress(paddle_l.move_down, "s")

# Ball
ball = Ball()

# Scoreboard
scoreboard = Scoreboard()
create_middle_line()

# Speed game
speed_levels = [0.05, 0.04, 0.03, 0.02]
index_speed = 0

# Turn on
game_is_on = True

while game_is_on:
    ball.move()

    # Collision with top wall and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddles
    if ball.distance(paddle_r) < 60 and ball.xcor() > 320 or ball.distance(paddle_l) < 60 and ball.xcor() < -320:
        ball.bounce_x()
        if index_speed < len(speed_levels) - 1:
            index_speed += 1

    # Paddle right miss the ball
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.update("left")
        index_speed = 0

    # Paddle left miss the ball
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.update("right")
        index_speed = 0

    time.sleep(speed_levels[index_speed])
    screen.update()
