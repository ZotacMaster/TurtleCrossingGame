import random
from turtle import Turtle, Screen
from obstacles import Obstacles
from player import Player
import time

from scoreboard import Scoreboard


screen = Screen()
screen.colormode(255)
screen.setup(600, 600)
screen.tracer(0)

player = Player()
obstacles = Obstacles()


screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")
scorebboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    for obs in obstacles.obstacles:
        # detect collision
        if player.distance(obs) < 20:
            game_is_on = False
            scorebboard.game_over()

    obstacles.create_obstacles()
    obstacles.move()

    # player crossing the finish line
    if player.is_at_finsih():
        player.goto(0, -290)
        scorebboard.increase_score()
        obstacles.level_up()
        time.sleep(1)
    time.sleep(0.1)

screen.exitonclick()