from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.carmaker()

    def carmaker(self):
        self.color(random.choice(COLORS))
        self.goto(x=300, y=(random.randrange(-200, 250, 30)))
        self.setheading(180)

    def carmove(self):
        if self.xcor() > -320:
            self.forward(STARTING_MOVE_DISTANCE)
        # else:
        #     self.carmaker()
        #

