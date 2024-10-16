from turtle import Turtle


class Pin(Turtle):
    def __init__(self, player_no):
        super().__init__()
        self.pos = 0
        self.shape("triangle")
        self.setheading(90)
        self.up()
        self.shapesize(1, 1.5)