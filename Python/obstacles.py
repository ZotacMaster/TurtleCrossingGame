from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCRIMENT = 10
class Obstacles:
    def __init__(self):
        self.obstacles = []
        self.speed = STARTING_MOVE_DISTANCE
    
    def move(self):
        """Move the obsticle by a random distance"""
        for obs in self.obstacles:
            obs.forward(-self.speed)
    
    def create_obstacles(self):
        """Creates obstacles on the screen"""
        chance = random.randint(1,10)
        if chance == 1:
            new_obs = Turtle("square")
            new_obs.penup()
            new_obs.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            new_obs.goto(280, random.randint(-250 , 250))
            new_obs.shapesize(stretch_wid=1, stretch_len=2)
            self.obstacles.append(new_obs)
    
    def level_up(self):
        """Increases the speed of the obstacles"""
        self.speed += MOVE_INCRIMENT
