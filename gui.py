from turtle import Screen
from player_line import Playerline
from ball import Ball
from playfield import Score
import time

# Setup the screen
play_field = Screen()
play_field.setup(width=800, height=600)
play_field.bgcolor("black")
play_field.title("Breakout")

# Turns animation off
play_field.tracer(0)

# Creates the player line
player_line = Playerline(x_pos=0, y_pos=-240, difficulty=7)

play_field.listen()


play_field.onkey(player_line.turn_right, "Right")
play_field.onkey(player_line.turn_left, "Left")


# Creates the ball
ball = Ball()

# Creates the score
score = Score()

def run_breakout(ball, playfield):
    game_is_running = True
    print(player_line.width())
    while game_is_running:

        screen_width = playfield.window_width()
        screen_height = playfield.window_height()
        half_screen_width = screen_width / 2
        half_screen_height = screen_height / 2

        time.sleep(ball.move_speed)
        # updates animation
        playfield.update()

        ball.move()

        player_line.goto(player_line.xcor(), -(half_screen_height - 60))

        # Detect Top collision
        if ball.ycor() > (half_screen_height - 15):
            ball.bounce_top()

        # Detect Wand collision
        if ball.xcor() > (half_screen_width - 25) or ball.xcor() < -(half_screen_width - 15):
            ball.bounce_walls()

        # Detect paddle collision
        if ball.distance(player_line) < 50 and ball.ycor() < -(half_screen_height - 85):
            ball.bounce_playerline()

        # Detect when ball leaves the table
        if ball.ycor() < -half_screen_height:
            ball.ball_reset()
            player_line.reset()

        # prevent player from going off screen
        if player_line.xcor() > half_screen_width - 20:
            player_line.turn_left()
        if player_line.xcor() < -half_screen_width + 20:
            player_line.turn_right()


run_breakout(ball, play_field)

play_field.exitonclick()