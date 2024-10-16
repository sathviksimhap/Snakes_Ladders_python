from turtle import Turtle, Screen
from pins import Pin
from positions import Positions
import time

#BOARD
Board = Screen()
Board.setup(560, 560)
Board.bgpic("board.PNG")

player = Pin(0)

i = 0
while True:
    time.sleep(.5)
    player.goto(Positions[i])
    i += 1






Board.exitonclick()