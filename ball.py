from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_distance_y = 10
        self.move_distance_x = 10

    def move(self):
        self.sety(self.ycor() + self.move_distance_y)
        self.setx(self.xcor() + self.move_distance_x)

    def bounce_y(self):
        self.move_distance_y *= -1

    def bounce_x(self):
        self.move_distance_x *= -1

    def reset_position(self):
        self.goto(0, 0)
