from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0


    def addScore(self):
        self.score += 1


    def SetupScore(self):
        self.hideturtle()
        self.goto(-100, 280)
        self.shape("square")
        self.color("white")
        self.penup()

    def UpdateScoreboard(self):
        self.hideturtle()
        self.addScore()
        self.goto(-100, 280)
        self.clear()
        self.write(f'Score = {self.score}', True, align='center', font=style)
        self.goto(100, 280)
        self.write(f'Highscore = {self.highscore}', True, align='center', font=style)




    def HighScore(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0



style = ('Courier', 20, 'italic')

