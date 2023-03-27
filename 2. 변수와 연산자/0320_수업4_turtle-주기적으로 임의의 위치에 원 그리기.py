#어러움 ㅠㅠ


import turtle
import random
turtle.title("마우스 이벤트 처리하기")    # 창 제목 변경
turtle.setup(600, 600)                    # 창 크기 변경

t = turtle.Pen()
t.speed(0)          # 가장 빠르게 그림
t.fillcolor("white")  

def Draw():     # 이벤트 처리 함수, (x, y) : 마우스 클릭 좌표
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    t.penup()
    t.goto(x, y)    # 마우스 클릭 좌표로 이동
    t.pendown()
    t.begin_fill()
    t.circle(10)    # 원을 그림
    t.end_fill()
    s.ontimer(Draw,100)
    
s = turtle.Screen()
s.ontimer(Draw,  1)  # 왼쪽 마우스 버튼 클릭 시 Draw 함수 실행
s.listen()

turtle.done()       # 이벤트 루프 시작
