#
# Author : Yousef
# this file is a part of the ping-pong game project
#

import turtle

ball = turtle.Turtle()  # create a new ball object
ball.speed(0)           # give maximum speed to the ball
ball.shape("square")    # determine shape of the ball 
ball.color("white")     # determine color of the ball
ball.penup()            # disable line drawing during ball's motion
ball.goto(0,0)          # position ball at the center
ball.dx = 2.5           # change amount in ball coordinates when moving
ball.dy = 2.5           # change amount in ball coordinates when moving


