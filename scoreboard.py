from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.sety(200)
        self.update(0)

    def update(self, left_or_right):
        self.clear()
        if left_or_right == "left":
            self.left_score += 1
        elif left_or_right == "right":
            self.right_score += 1
        self.write(f"{self.left_score}     {self.right_score}", align="center", font=("Courier", 50, "normal"))


def create_middle_line():
    start_y = -300
    segment = Turtle()
    segment.penup()
    segment.hideturtle()
    segment.setheading(90)
    segment.color("white")
    segment.sety(start_y)
    segment.pensize(5)
    for step in range(30):
        if step % 2 == 0:
            segment.penup()
        else:
            segment.pendown()
        segment.forward(20)
