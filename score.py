from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt', 'r') as file:
            self.high_score = int(file.read())
        self.penup()
        self.color("pink")
        self.hideturtle()
        self.setposition(-20, 270)
        self.write(f"Score: {self.score},  High Score: {self.high_score}", align='center', font=('arial', 16, 'normal'))

    #Cambia el marcador cada que se come un cuadrito
    def change_score(self):
        self.score += 1
        self.clear()
        self.setposition(-20, 270)
        #Si el marcador actual es mayor que el high-score, se actualiza y se guarda en high_score.txt
        with open('high_score.txt', 'r') as f:
            if self.score > int(f.read()):
                self.high_score = self.score
        self.write(f"Score: {self.score},  High Score: {self.high_score}", align='center', font=('arial', 16, 'normal'))
