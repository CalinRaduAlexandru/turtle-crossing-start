from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.create_car()
        self.move_continues()

    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len = 2.5, stretch_wid = 1)
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_continues(self):
        for car in self.all_cars:
            car.bk(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.speed += 100





