from turtle import Turtle

#Made a class called Paddle

class Paddle(Turtle):

    #Gets the shape and color of the paddle
    #Streachs the paddle to a long certain length
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    #To make the paddle go up 
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    #To make the paddle go down
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
