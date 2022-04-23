from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.goto(0, -220)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_top(self):
        self.y_move *= -1
        # self.move_speed *= 0.9

    def bounce_walls(self):
        self.x_move *= -1
        # self.move_speed *= 0.9

    def bounce_playerline(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.goto(0, -220)
        self.move_speed = 0.1
        self.bounce_playerline()