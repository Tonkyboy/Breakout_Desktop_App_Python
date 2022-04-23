from turtle import Turtle

STEP = 60
PLAYERLINE_WIDTH = 1

class Playerline(Turtle):
    def __init__(self, x_pos, y_pos, difficulty):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid= PLAYERLINE_WIDTH , stretch_len=difficulty)
        self.color("white")
        self.setpos(x=x_pos, y=y_pos)

    def turn_right(self):
        x_cord = self.xcor()
        self.setx(x_cord + STEP)


    def turn_left(self):
        x_cord = self.xcor()
        self.setx(x_cord - STEP)

    def reset(self):
        self.setpos(0,-250)
