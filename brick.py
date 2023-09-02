from turtle import Turtle

class Brick(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_len=2.6, stretch_wid=0.6)
        self.color("red")