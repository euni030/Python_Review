import turtle
# DrawCircle . 함수를	작성하라
t = turtle.Pen()

def DrawCircle(x,y,r=10, p_c="black",f_c="white"):
    t.penup()
    t.goto(x,y-r)
    t.pendown()
    t.begin_fill() 
    t.pencolor(p_c)
    t.fillcolor(f_c)
    t.circle(r)
    t.end_fill()
    
            
               

DrawCircle(0, 0)
DrawCircle(100, 100, 100)
DrawCircle(-100, 100, 50, "red", "green")
DrawCircle(0, -100, 50, "blue", "yellow")
    
turtle.done()
