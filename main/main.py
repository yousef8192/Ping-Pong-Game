

import time
import turtle
from paddles import *
from ball import *



### function definitions ############################################################################################################################################## 

def move_paddleA_up():
    if paddleA.ycor() < (window_height/2)-60 :
        paddleA.sety(paddleA.ycor()+20)

def move_paddleA_down():
    if paddleA.ycor() > -(window_height/2)+60 :
        paddleA.sety(paddleA.ycor()-20)

def move_paddleB_up():
    if paddleB.ycor() < (window_height/2)-60 :
        paddleB.sety(paddleB.ycor()+20)

def move_paddleB_down():
    if paddleB.ycor() > -(window_height/2)+60 :
        paddleB.sety(paddleB.ycor()-20)

def ball_hit_paddle():
    if (ball.xcor()-10 <= paddleA.xcor()+10):
        if (((paddleA.ycor()+60)>=(ball.ycor()-10)) and ((paddleA.ycor()-60)<=(ball.ycor()+10))):
            return True
    if (ball.xcor()+10 >= paddleB.xcor()-10):
        if (((paddleB.ycor()+60)>=(ball.ycor()-10)) and ((paddleB.ycor()-60)<=(ball.ycor()+10))):
            return True
    return False
        

def ball_hit_horizontal_walls():
    if ball.ycor()+10 >= window_height/2:
        return True
    if ball.ycor()-10 <= -window_height/2:
        return True
    return False

def ball_hit_red_wall():
    if ball.xcor()+10 >= window_width/2:
        return True
    return False

def ball_hit_blue_wall():
    if ball.xcor()-10 <= -window_width/2:
        return True
    return False

### window ############################################################################################################################################## 

window = turtle.Screen()                                    # create the main window of the game and store it in a variable
window.title("Ping-Pong Game")                              # title
window.bgcolor("black")                                     # background color
window_width = 1000                                         # window width
window_height = 800                                         # window height
window.setup(width=window_width, height=window_height)      # dimensions
window.tracer(0)                                            # disable auto update of the window (bec we'll update it manually)

### score ##############################################################################################################################################

blue_score = 0                                              # variable to hold blue player's score
red_score = 0                                               # variable to hold red  player's score
score_label = turtle.Turtle()                               # create an object for the Score Label
score_label.speed(0)                                        # set its speed to maximum
score_label.color("white")                                  # set the label text color
score_label.penup()                                         # disable automatic line drawing during 
score_label.hideturtle()                                    # hide the turtle object itself since we are just interested in the label
score_label.goto(0, (window_height/2)-50)                   # adjust position of the label to be oriented at the top
score_label.write("Blue: {}  |  Red: {}".format(blue_score, red_score), align="center", font=("Courier",24,"normal"))


### control ##############################################################################################################################################

window.listen()                                     # prompt the window to keep listening for keystrokes
window.onkeypress(move_paddleA_up, "w")             # 'w'       moves the blue Player upwards
window.onkeypress(move_paddleA_down, "s")           # 's'       moves the blue Player downwards
window.onkeypress(move_paddleB_up, "Up")            # 'Up'      moves the red  Player upwards
window.onkeypress(move_paddleB_down, "Down")        # 'Down'    moves the red  Player downwards


### start of the program ##############################################################################################################################################

while True:

    window.update()                     # keep updating the window

    ball.setx(ball.xcor()+ball.dx)      # move the ball (change it x-coordinate)
    ball.sety(ball.ycor()+ball.dy)      # move the ball (change it y-coordinate)

    if ball_hit_paddle():               # if the ball hits either of the paddles bounce it back
        ball.dx *= -1 

    if ball_hit_horizontal_walls():     # if the ball hits either of the horizontal walls (up or down) bounce it back
        ball.dy *= -1 
   
    if ball_hit_red_wall():              
        # if the ball hits the wall of the red player
        # simply increase the score of the blue player
        # then redraw the score on the screen
        # then reset the ball to the center and reverse its motion to go towards the blue player
        blue_score += 1
        score_label.clear()
        score_label.write("Blue: {}  |  Red: {}".format(blue_score, red_score), align="center", font=("Courier",24,"normal"))
        ball.dx *= -1 
        ball.dy *= -1 
        ball.setx(0)       
        ball.sety(0)       

    if ball_hit_blue_wall():
        # if the ball hits the wall of the blue player
        # simply increase the score of the red player
        # then redraw the score on the screen
        # then reset the ball to the center and reverse its motion to go towards the red player
        red_score += 1
        score_label.clear()
        score_label.write("Blue: {}  |  Red: {}".format(blue_score, red_score), align="center", font=("Courier",24,"normal"))
        ball.dx *= -1 
        ball.dy *= -1 
        ball.setx(0)
        ball.sety(0)       

    time.sleep(0.01)            # delay for updating the screen
   


    






