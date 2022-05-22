from turtle import Screen, Turtle
from snake import Snec, segmente
from food import Food
import time
from test import ScoreBoard, style

score = 0
scorenebun = ScoreBoard()
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game!")
my_screen.tracer(0)
snake = Snec()
food = Food()
snake.hideturtle()
scorenebun.SetupScore()
scorenebun.write(f'Score = {score}', True, align='center', font=style)
scorenebun.goto(100, 280)
scorenebun.write(f'HighScore = {scorenebun.highscore}', True, align='center', font=style)

#

my_screen.onkey(key="w", fun=snake.up)
my_screen.onkey(key="a", fun=snake.left)
my_screen.onkey(key="s", fun=snake.down)
my_screen.onkey(key="d", fun=snake.right)

#
#
my_screen.listen()


snake.speed = 15
game_running = True
while game_running:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    snake.head.forward(snake.speed)

    # collision with the tail
    for m in range(3, len(segmente), 1):
        if snake.head.distance(segmente[m]) < 5:
            game_running = False
            scorenebun.HighScore()
            my_screen.clear()
            my_screen.bgcolor("black")
            snake.color("white")
            snake.goto(0, 0)
            snake.write('Game over!', True, align='center', font=style)

    # collision with the food and also spawning the food in another random location on screen
    if snake.head.distance(food) < 20:
        food.warp_food()
        score += 1
        snake.speed += 1
        scorenebun.UpdateScoreboard()

        # adding another part to the snake after eating the food
        for n in range(score):
            another = Turtle("square")
            another.color("black")
            another.penup()
            another.color("white")
            segmente.append(another)


#
#
#
my_screen.exitonclick()
#
