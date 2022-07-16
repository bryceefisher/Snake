from turtle import Turtle
from snake import Snake
with open("high_score.txt") as file:
    contents = file.read()
    file.close()
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.high_score = contents
        self.color("white")
        self.goto(0, 270)


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}: High Score: {self.high_score}", False, ALIGNMENT, FONT)


    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.score}")
            self.score = 0
            self.update_scoreboard()


    def snake_eat(self):
        self.score += 1
        self.update_scoreboard()
