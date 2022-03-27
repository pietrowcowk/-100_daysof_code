from turtle import Screen, Turtle
import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('white')
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up, 'Up')
screen.onkeypress(right_paddle.go_down, 'Down')
screen.onkeypress(left_paddle.go_up, 'w')
screen.onkeypress(left_paddle.go_down, 's')

while True:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed) #to slow down ball

#Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 350 or ball.distance(left_paddle) < 50 and ball.xcor() > -350:
        ball.bounce_x()

#Detect missing the ball - right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.right_point()

#Detect missing the ball - left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.left_point()














screen.exitonclick()