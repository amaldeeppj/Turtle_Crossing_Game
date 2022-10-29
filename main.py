import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

num_cars = 10
car_speed = 0.1
car_manager = []

# def generate_cars(cars):
#     for i in range(cars):
#         if random.choice([True, False]):
#             car_manager.append(CarManager())


screen = Screen()
screen.title("Turtle Cross")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
#car_manager = CarManager()
#generate_cars(num_cars)


screen.listen()
screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(car_speed)
    screen.update()
    # car_manager = CarManager(random.randint(0, 10))
    #car_manager.carmove()

    # Player crosses
    if player.ycor() >= 280:
        player.next_level()
        scoreboard.level_up()
        car_speed *= 0.9

    if random.choice([True, False, False, False, False, False]):
        car_manager.append(CarManager())

    # Detect collition
    for car in car_manager:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
        else:
            car.carmove()

screen.exitonclick()


