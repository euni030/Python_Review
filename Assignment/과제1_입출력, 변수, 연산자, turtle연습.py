가로=int(input("가로 길이:"))
세로=int(input("세로 길이:"))
색깔=input("채움색깔(“red”, “green”, “blue”) 중 하나를 입력:")

print("직사각형의 가로길이:",가로)
print("직사각형의 가로길이:",세로)
print("직사각형의 면적:",가로*세로)


import turtle       # turtle 모듈 import

t = turtle.Pen()                # 펜 객체 생성
t.fillcolor(색깔)
t.begin_fill()  #터틀의 색으로 도형 내부를 칠하려면 begin_fill()과 end_fill()을 짝 맞춰 실행해야함

t.forward(가로); t.right(90)     # 사각형 그리기
t.forward(세로); t.right(90)
t.forward(가로); t.right(90)
t.forward(세로)


t.penup()                       # 펜 들고 이동
t.goto(0, 0)
t.pendown()

t.forward(세로); t.right(90)     # 사각형 그리기
t.forward(가로); t.right(90)
t.forward(세로); t.right(90)
t.forward(가로)

t.penup()                       # 펜 들고 이동
t.goto(0, 0)
t.pendown()

t.forward(가로); t.right(90)     # 사각형 그리기
t.forward(세로); t.right(90)
t.forward(가로); t.right(90)
t.forward(세로)

t.penup()                       # 펜 들고 이동
t.goto(0, 0)
t.pendown()

t.forward(세로); t.right(90)     # 사각형 그리기
t.forward(가로); t.right(90)
t.forward(세로); t.right(90)
t.forward(가로)

t.end_fill()

turtle.done()       # 이벤트 루프 시작


