import turtle
import random
t = turtle.Turtle()  #객체 생성(거북이 생성)

# DrawSquare 함수를 만든다.
def DrawSquare(x,y,r):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.speed(0)
    
    for i in range(0,4):
        t.forward(2*r)
        t.left(90)
    

# DrawCircle 함수를 만든다.
def DrawCircle(x,y,r):
    t.penup()
    t.goto(x,y-r)
    t.pendown()
    t.speed(0)
    
    t.circle(r)
    
def DrawRandomCircles(n):
    for i in range(n):
        r=random.randint(1,20)
        x=random.randint(-199+r,199-r)
        y=random.randint(-199+r,199-r)
        DrawCircle(x,y,r)


def main():
    DrawSquare(-200, -200, 200)
    circle_count = eval(turtle.textinput("", "원의 개수 : "))
    DrawRandomCircles(circle_count)
    # 사각형 내에 circle_count 개수만큼의 원을 그린다.
    

main()   

turtle.done()