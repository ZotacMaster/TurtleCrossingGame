from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-250, 270)
        self.display(size=15)

    def display(self, size):
        self.write(arg=f"Level {self.score}", align="center", font=("Courier", size, "bold"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.display(size=15)
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over", align="center", font=("Courier", 20, "bold"))