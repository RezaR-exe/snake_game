from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segmente = []




class Snec(Turtle):
    def __init__(self):
        for i in starting_positions:
            new_part = Turtle("square")
            new_part.color("white")
            new_part.penup()
            new_part.goto(i)
            segmente.append(new_part)
        super().__init__()
        self.head = segmente[0]


    def move(self):
        for seg_num in range(len(segmente) - 1, 0, -1):
            new_x = segmente[seg_num - 1].xcor()
            new_y = segmente[seg_num - 1].ycor()
            segmente[seg_num].goto(new_x, new_y)
            # segmente[0].forward(10)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def right(self):
        self.head.setheading(0)

    def left(self):
        self.head.setheading(180)

    def speedIncrease(self):
        self.speed += 100




