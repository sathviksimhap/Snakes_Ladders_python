from turtle import Turtle
import random
import time
from positions import Positions

class Pin(Turtle):
    def __init__(self):
        super().__init__()
        self.pos = 0
        self.shape("triangle")
        self.up()
        self.setheading(90)
        self.goto(-275, -240)
        self.shapesize(1, 1.5)

    def move(self):
        goal = random.randint(1, 6)
        goal_pos = self.pos + goal
        while self.pos != goal_pos:
            self.pos += 1
            self.goto(Positions[self.pos])
            time.sleep(0.2)
