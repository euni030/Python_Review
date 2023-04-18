import turtle
import math

t=turtle.Pen()

def DrawTriangle(length):
    for i in range(3):
        t.forward(length)
        t.left(120)
        
    if length <20:
        return
    
    length=length/2
    t.forward(length)
    t.left(60)
    DrawTriangle(length)

length=300
t.penup()
t.goto(-length/2, -(length*math.sin(math.radians(60))))
t.pendown()
DrawTriangle(length)

turtle.done()