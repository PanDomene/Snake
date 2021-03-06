from turtle import Turtle


#Creamos la serpiente
class Snake:
    def __init__(self):
        #tamaño inicial: 3 unidades
        self.size = 3
        self.segments = []
        for i in range(self.size):
            self.segments.append(Turtle(shape='circle'))
            self.segments[i].color("white")
            self.segments[i].penup()
            self.segments[i].setx(-20 * i)
        self.head = self.segments[0]
    #Cada unidad de tiempo hacemos avanzar a la serpiente 1 unidad de distancia hacia adelante.
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            self.segments[segment].goto(self.segments[segment - 1].pos())
        self.head.forward(14)

    #Damos movilidad a la serpiente
    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    #añade una unidad de longitud más a la serpiente.
    def grow(self):
        new_segment = Turtle("circle")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(self.segments[self.size-1].position())
        self.segments.append(new_segment)
        self.size += 1
