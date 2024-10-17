from turtle import Turtle
import random
import time
from mydata import POSITIONS, SNAKES, LADDERS

class Pin(Turtle):
    def __init__(self):
        super().__init__()
        self.pos = 0
        self.shape("triangle")
        self.up()
        self.setheading(90)
        self.goto(-275, -240)
        self.shapesize(1, 1.5)


    def roll(self):
        goal = random.randint(1, 6)
        goal_pos = self.pos + goal
        self.move(goal_pos)

        if self.pos in SNAKES.keys():
            self.goto(POSITIONS[SNAKES[self.pos]])
            self.pos = SNAKES[self.pos]

        elif self.pos in LADDERS.keys():
            self.goto(POSITIONS[LADDERS[self.pos]])
            self.pos = LADDERS[self.pos]

    def move(self, goal):
        while self.pos != goal:
            self.pos += 1
            self.goto(POSITIONS[self.pos])
            time.sleep(0.2)
