from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -270)
    def up(self):
        self.forward(10)
    def down(self):
        self.forward(-10)
    
    def is_at_finsih(self):
        return self.ycor() > 280