import turtle

t=turtle.pen()

num=int(input("한 변의 길이 입력:"))

t.forward(num); t.right(72)
t.forward(num); t.right(72)
t.forward(num); t.right(72)
t.forward(num); t.right(72)
t.forward(num)

t.penup()
t.pendown()

turtle.done()
