from STT import *
from TTS import *
import turtle
from turtle import *

def voicedraw():
    tts("Speak a thing to draw")
    drawquery=rstt()
    print("drawquery : ",drawquery)
    if drawquery.find('circle')!=-1:
        drawcircle()
    elif drawquery.find('rectangle')!=-1:
        drawrectangle()
    elif drawquery.find('triangle')!=-1:
        drawtriangle()
    elif drawquery.find('star')!=-1:
        drawstar()
    elif drawquery.find('square')!=-1:
        drawsquare()
    else:
        drawtext(drawquery)
    

def drawcircle():
    turtle.circle(80)
    turtle.exitonclick()

def drawsquare():
    # drawing first side
    turtle.up()
    turtle.goto(-150,-100)
    turtle.down()
    turtle.forward(400) # Forward turtle by s units
    turtle.left(90) # Turn turtle by 90 degree
    
    # drawing second side
    turtle.forward(400) # Forward turtle by s units
    turtle.left(90) # Turn turtle by 90 degree
    
    # drawing third side
    turtle.forward(400) # Forward turtle by s units
    turtle.left(90) # Turn turtle by 90 degree
    
    # drawing fourth side
    turtle.forward(400) # Forward turtle by s units
    turtle.left(90) # Turn turtle by 90 degree
    turtle.exitonclick()
    
def drawrectangle():
    turtle.up()
    turtle.goto(-150,-100)
    turtle.down()
    for _ in range(4):
   
  # drawing length
        if _% 2 == 0:
            turtle.forward(400) # Forward turtle by l units
            turtle.left(90) # Turn turtle by 90 degree
        
        # drawing width
        else:
            turtle.forward(200) # Forward turtle by w units
            turtle.left(90)
            
    turtle.exitonclick()
def drawtriangle():
    turtle.forward(100) # draw base
    turtle.left(120)
    turtle.forward(100)
    
    turtle.left(120)
    turtle.forward(100)
    turtle.exitonclick()

def drawstar():
# executing loop 5 times for a star
    for i in range(5):
    
            # moving turtle 100 units forward
            turtle.forward(100)
    
            # rotating turtle 144 degree right
            turtle.right(144)
    turtle.exitonclick()
    

def drawtext(drawquery):
    turtle.penup()
    turtle.setposition(-400,300)
    drawquery="Shape Not Found \n"+drawquery
    turtle.write(drawquery, font=("Arial", 16, "normal"))
    turtle.exitonclick()

def tdraw(query):
    turtle.penup()
    turtle.setposition(-400,300)
    turtle.write(query, font=("Arial", 16, "normal"))
    turtle.exitonclick()