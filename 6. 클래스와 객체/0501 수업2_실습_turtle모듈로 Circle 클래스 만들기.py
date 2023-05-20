import turtle
import random

t=turtle.Pen()

class Circle:
    def __init__(self, x=0,y=0,r=10,color="black"):
        self.x=x
        self.y=y
        self.r=r
        self.color=color
    
    def Draw(self,t):
        t.penup() 
        t.goto(self.x, self.y- self.r)
        t.pendown() 
        t.pencolor(self.color)
        t.circle(self.r)
        
circles=[]
for i in range(10):
    x,y=random.randint(-300,300), random.randint(-300,300)
    r=random.randint(10,80)
    color=random.choice(["black","red","green","blue","yellow"])
    circles.append(Circle(x,y,r,color))

for cir in circles:
    cir.Draw(t)

turtle.done()