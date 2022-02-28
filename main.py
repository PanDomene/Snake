from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time


#Código base del juego.
def game():
    #UI
    screen = Screen()
    screen.setup(600, 600)
    screen.title('Snake')
    screen.bgcolor('black')
    screen.tracer(0)
    snake = Snake()
    food = Food()
    score = Scoreboard()
    screen.listen()
    screen.onkey(snake.turn_up, "Up")
    screen.onkey(snake.turn_down, "Down")
    screen.onkey(snake.turn_left, "Left")
    screen.onkey(snake.turn_right, "Right")
    snake_is_alive = True

    #Jugabilidad
    while snake_is_alive:
        screen.update()
        time.sleep(0.03)
        snake.move()
        #Si come crece 4 unidades
        if snake.head.distance(food.position()) < 12:
            food.move()
            snake.grow()
            snake.grow()
            snake.grow()
            snake.grow()
            score.change_score()
            with open('high_score.txt', 'w') as file:
                file.write(str(score.high_score))
        #Checar si chocó con paredes
        if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
            snake_is_alive = False
        #Checar si chocó consigo misma
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                snake_is_alive = False
    #Volver a jugar
    otra_vez = screen.textinput("Pelas!", "Quieres jugar otra vez? (si/no)")
    if otra_vez.lower() == 'si' or otra_vez == 's':
        screen.clear()
        game()

    screen.exitonclick()


game()
