from turtle import Turtle

#Class Scoreboard
class Scoreboard(Turtle):

    #
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    #This function up dates the score board in the middle of the screen
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    #Keeps track how many points the left side has
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    #Keeps track how many points the right side has
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
