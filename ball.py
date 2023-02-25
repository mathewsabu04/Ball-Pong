from turtle import Turtle

#Made a class called Turtle 

class Ball(Turtle):
    
    #Made the shape of the ball and color
    #Used penup() so the ball doesnt leave extra lines on the board
    #Set the speed of the ball at 0.1
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    #This makes it so the ball actually moves around the board
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    #This checks the ball bouncing from the why coordinate

    def bounce_y(self):
        self.y_move *= -1

    #This checks the ball bouncing from the x coordinate
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    #This resets the position of the ball
    
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
