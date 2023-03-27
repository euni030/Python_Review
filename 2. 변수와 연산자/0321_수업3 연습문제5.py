import turtle

t=turtle.Pen()
t.speed(0)
t.pensize(5)

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor("blue")
t.circle(35)

t.penup()
t.goto(80,100)
t.pendown()
t.pencolor("black")
t.circle(35)

t.penup()
t.goto(160,100)
t.pendown()
t.pencolor("red")
t.circle(35)

t.penup()
t.goto(50,45)
t.pendown()
t.pencolor("yellow")
t.circle(35)

t.penup()
t.goto(130,45)
t.pendown()
t.pencolor("green")
t.circle(35)

turtle.done()
