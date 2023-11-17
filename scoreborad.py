from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
class Scoreborad(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("D:\Python Course\python course by Angela\snake _game\data.txt") as data:
            self.high_score = int(data.read())

        self.color("orange")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake _game\data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
