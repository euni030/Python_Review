#사진찍어둔거 보고 수정하기ㅇㅇ

import turtle
turtle.title("마우스 이벤트 처리하기")    # 창 제목 변경
turtle.setup(400, 300)                    # 창 크기 변경

t = turtle.Pen()
t.speed(0)          # 가장 빠르게 그림
t.fillcolor("red")  # 빨간색으로 채움

def Draw(x, y,c):     # 이벤트 처리 함수, (x, y) : 마우스 클릭 좌표
    t.penup()
    t.goto(x, y)    # 마우스 클릭 좌표로 이동
    t.pendown()
    t.fillcolor(c)
    t.begin_fill()
    t.circle(20)    # 원을 그림
    t.end_fill()

s = turtle.Screen()
s.onclick(lambda x, y: Draw(x,y,"red"),1)  # 왼쪽 마우스 버튼 클릭 시 Draw 함수 실행
s.onclick(lambda x, y: Draw(x,y,"blue"),3)  # 오른쪽 마우스 버튼 클릭 시 Draw 함수 실행
s.listen()

turtle.done()       # 이벤트 루프 시작
