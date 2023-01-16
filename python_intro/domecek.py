from turtle import *
import math
import random

def maluj(a):
    left(90)
    forward(a)
    
    right(90)
    forward(a)
    
    right(45 + 90)
    forward(round(math.sqrt(a**2 * 2)))
    
    left(45 + 90)
    forward(a)
    
    left(90)
    forward(a)
    
    left(45)
    forward(round(math.sqrt(a**2 /2)))
    
    left(90)
    forward(round(math.sqrt(a**2 /2)))
    
    left(90)
    forward(round(math.sqrt(a**2 * 2)))
    
    left(45)

penup()
goto(-400, 0)
pendown()

for i in range(20):
    maluj(random.randint(25, 100))
    

exitonclick()
