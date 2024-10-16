from turtle import Turtle


class Pin(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.up()
        self.goto(-245, -240)