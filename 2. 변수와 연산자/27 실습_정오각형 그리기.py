import turtle

t=turtle.Pen()

num=int(input("한 변의 길이 입력:"))

t.forward(num); t.right(72)
t.forward(num); t.right(72)
t.forward(num); t.right(72)
t.forward(num); t.right(72)
t.forward(num)

t.penup()
t.goto(200,200)
t.pendown()

turtle.done()
