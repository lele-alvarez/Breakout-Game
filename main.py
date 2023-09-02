from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time
from random import randint

BRICK_INITIAL_X = -360 
BRICK_INITIAL_Y = 200


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

# Display bricks
bricks = []
colors = ["blue", "red", "yellow", "gray", "orange", "green", "violet", "turquoise"]
for i in range(10):
    for j in range(14):
        brick = Brick((BRICK_INITIAL_X, BRICK_INITIAL_Y))
        number = randint(0,7)

        brick.color(colors[number])
        bricks.append(brick)
        BRICK_INITIAL_X += 55
    BRICK_INITIAL_X = -360
    BRICK_INITIAL_Y -= 16

paddle = Paddle()
ball = Ball()
score = Scoreboard()


game_is_on = False
# Paddle controls
screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
# Detect collision with wall (Bounce)
    if ball.xcor() > 385 or ball.xcor() < - 385:
        ball.bounce_x()

# Detect collision with roof (Bounce)
    if ball.ycor() > 285:
        ball.bounce_y()

# Detect collision with the paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -225:
        ball.bounce_y()

# Detect when paddle misses
    if ball.ycor() < -250:
        score.lifes_count()
        paddle.reset_position()
        ball.reset_position()
        time.sleep(2)
        if score.get_lifes() == 0:
            game_is_on = False
            score.game_over()
            
# Detect colission with brick
    for brick in bricks:
        if ball.distance(brick)< 35 and brick.pencolor() == "gray":
            ball.bounce_y()
        elif ball.distance(brick) < 35:
            ball.bounce_y()
            brick.hideturtle()
            bricks.remove(brick)
            score.point()
            if score.get_score() % 10 == 0:
                ball.increase_speed()
            break
            

screen.exitonclick()