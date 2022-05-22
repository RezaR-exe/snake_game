from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.warp_food()

    def warp_food(self):
        my_x = random.randint(-280, 280)
        my_y = random.randint(-280, 280)
        self.goto(my_x, my_y)


