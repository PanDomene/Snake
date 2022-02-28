import random
from turtle import Turtle


#Al inicio del juego y cada vez que se come, crea un cuadrito de comida nuevo en una ubicación al azar
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(0.3, 0.3)
        self.speed("fastest")
        self.color("yellow")
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def move(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
