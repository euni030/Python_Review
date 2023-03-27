#나중에 다시 하기
 
import turtle

t=turtle.Pen()

num=int(input("한 변의 길이 입력:"))

t.forward(num); t.right(90)
t.forward(num); t.right(90)
t.forward(num); t.right(90)

#t.fillcolor("blue")
#t.begin_fill()  #터틀의 색으로 도형 내부를 칠하려면 begin_fill()과 end_fill()을 짝 맞춰 실행해야함
t.forward(num);t.right(30)
t.forward(num);t.right(60)
t.forward(num);t.right(30)
t.forward(num);t.right(30)
t.forward(num)
"""
t.forward(num);t.right(60)
t.forward(num);t.right(60)
t.forward(num);t.right(120)
t.forward(num);t.right(60)
t.forward(num);t.right(60)
t.forward(num);t.right(120)
t.forward(num);t.right(60)
t.forward(num);t.right(60)
"""

t.penup()
t.goto(200,200)
t.pendown()
#t.end_fill()

turtle.done()
