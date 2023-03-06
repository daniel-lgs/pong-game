from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)

    def move_up(self):
        current_y = self.ycor()
        self.sety(current_y + 50)

    def move_down(self):
        current_y = self.ycor()
        self.sety(current_y - 50)
