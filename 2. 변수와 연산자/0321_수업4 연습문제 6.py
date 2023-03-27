#미해결 


import turtle

t = turtle.Pen()
t.speed(0)          # 가장 빠르게 그림


def Move(x,y):     # 이벤트 처리 함수, (x, y) : 마우스 클릭 좌표

    t.penup()
    t.goto(x, y)    # 마우스 클릭 좌표로 이동
    t.pendown()

    
s=turtle.Screen()
s.onclick(Move,1)
s.listen()

turtle.done()
    
