from turtle import Turtle, Screen
from pins import Pin

#BOARD
Board = Screen()
Board.setup(560, 560)
Board.bgpic("board.PNG")

player = Pin()

Board.listen()
Board.onkey(player.roll, "a")






Board.exitonclick()