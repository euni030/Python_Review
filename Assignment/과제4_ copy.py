import turtle
import random


class Shape(turtle.Pen):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
    
    def Draw(self, x, y, color):
        self.pencolor(color)
        self.penup()
        self.goto(x, y)
        self.pendown()
        self.dot()
    
    def Move(self, x, y):
        self.penup()
        self.goto(x, y)
        self.pendown()
    
    def Erase(self):
        self.pencolor("white")
        self.dot()

class Circle(Shape):
    def __init__(self):
        super().__init__()
    
    def Draw(self, x, y, color, r):
        super().Draw(x, y, color)
        self.circle(r)

class Rect(Shape):
    def __init__(self):
        super().__init__()
    
    def Draw(self, x, y, color, width, height):
        super().Draw(x, y, color)
        self.begin_fill()
        for i in range(2):
            self.forward(width)
            self.right(90)
            self.forward(height)
            self.right(90)
        self.end_fill()

# 도형 개수 입력 받기
num_shapes = int(input("도형의 개수를 입력하세요: "))

# 무작위로 Circle 또는 Rect 객체 생성하고 shapes 리스트에 추가하기
shapes = []
for i in range(num_shapes):
    rand_x = random.randint(-200, 200)
    rand_y = random.randint(-200, 200)
    rand_color = random.choice(["red", "green", "blue"])
    if random.randint(0, 1) == 0:
        rand_r = random.randint(10, 50)
        shape = Circle()
        shape.Draw(rand_x, rand_y, rand_color, rand_r)
    else:
        rand_width = random.randint(10, 70)
        rand_height = random.randint(10, 70)
        shape = Rect()
        shape.Draw(rand_x, rand_y, rand_color, rand_width, rand_height)
    shapes.append(shape)

# 삭제할 도형 개수 입력 받기
num_remove = int(input("삭제할 도형의 개수를 입력하세요: "))

# shapes 리스트로부터 무작위로 도형 삭제하기
for i in range(num_remove):
    if len(shapes) > 0:
        shape = random.choice(shapes)
        shape.Erase("white")
        shapes.remove(shape)

turtle.done()
