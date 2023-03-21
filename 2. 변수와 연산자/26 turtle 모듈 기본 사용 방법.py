import turtle       # turtle 모듈 import

t = turtle.Pen()                # 펜 객체 생성

t.forward(100); t.right(90)     # 사각형 그리기
t.forward(100); t.right(90)
t.forward(100); t.right(90)
t.forward(100)

t.penup()                       # 펜 들고 이동
t.goto(-200, -100)
t.pendown()

t.forward(100); t.right(90)     # 사각형 그리기
t.forward(100); t.right(90)
t.forward(100); t.right(90)
t.forward(100)

turtle.done()       # 이벤트 루프 시작
