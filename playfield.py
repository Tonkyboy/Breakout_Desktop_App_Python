from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.update_score()



    def update_score(self, ):
        self.goto(350, 250)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))
        self.goto(250, 250)
        self.write("Score", align="center", font=("Courier", 40, "normal"))