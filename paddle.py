from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(0, -250)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")

    def move_right(self):
        if self.xcor() < 340:
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto( new_x, self.ycor())
        else:
            self.goto(340, self.ycor())

    def move_left(self):
        if self.xcor() > -350:
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto( new_x, self.ycor())
        else:
            self.goto(-350, self.ycor())

    def reset_position(self):
        self.goto(0, -250)
