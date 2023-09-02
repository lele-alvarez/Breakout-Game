from turtle import Turtle

FONT = ("Comic Sans MS", 50, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("grey")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.lifes = 3
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-200, 210)
        self.write(f"Score: {self.score}", align="center", font=FONT)
        self.goto(200, 210)
        self.write(f"Lifes: {self.lifes}", align="center", font=FONT)

    def point(self):
        self.score += 1
        self.score_update()

    def lifes_count(self):
        self.lifes -= 1
        self.score_update()

    def get_score(self):
        return self.score
    
    def get_lifes(self):
        return self.lifes
    
    def score_reset(self):
        self.score = 0
        self.lifes = 3
        self.score_update()

    def game_over(self):
        self.goto(0, -100)
        self.write(f"GAME OVER", align="center", font=FONT)
        