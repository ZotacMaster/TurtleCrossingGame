from turtle import Turtle
import random

class Obstacles(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(300, random.randint(-300 , 300))
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color(r, g, b)
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=4)
    
    def move(self):
        self.forward(random.randint(10, 50))
    
