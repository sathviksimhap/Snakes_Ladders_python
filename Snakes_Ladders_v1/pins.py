from turtle import Turtle


class Pin(Turtle):
    def __init__(self, player_no):
        super().__init__()
        self.shape("triangle")
        self.up()