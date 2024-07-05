#
# Author : Yousef
# this file is a part of the ping-pong game project
#

import turtle

window_width = 1000                                 # window width
window_height = 800                                 # window height

paddleA = turtle.Turtle()                           # create a new paddle object
paddleA.speed(0)                                    # give maximum speed to the paddle 
paddleA.shape("square")                             # determine shape of the paddle 
paddleA.color("blue")                               # determine color of the paddle
paddleA.penup()                                     # disable line drawing during paddle's motion
paddleA.shapesize(stretch_wid=6, stretch_len=1)     # determine size of the paddle
paddleA.goto(-(window_width/2)+10,0)                # orient the paddle to its startup position

paddleB = turtle.Turtle()                           # create a new paddle object
paddleB.speed(0)                                    # give maximum speed to the paddle 
paddleB.shape("square")                             # determine shape of the paddle 
paddleB.color("red")                                # determine color of the paddle
paddleB.penup()                                     # disable line drawing during paddle's motion
paddleB.shapesize(stretch_wid=6, stretch_len=1)     # determine size of the paddle
paddleB.goto((window_width/2)-15,0)                 # orient the paddle to its startup position





