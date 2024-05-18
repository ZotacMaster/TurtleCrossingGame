import random
from turtle import Turtle, Screen
from obstacles import Obstacles
from player import Player
import time

screen = Screen()
screen.colormode(255)
screen.screensize(300, 300)
screen.tracer(0)

player = Player()
def generate():
    obsticle_list = []
    for i in range(10):
        obsticle_list.append(Obstacles()) 
    return obsticle_list

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    choice_obsticle = random.choice(generate())
    choice_obsticle.move()
    time.sleep(0.1)

screen.exitonclick()