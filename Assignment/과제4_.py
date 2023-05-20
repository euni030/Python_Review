import turtle
import random
turtle.setup(500,500)

#Shape클래스
class Shape(turtle.Pen):
    def __init(self,x,y):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.x=x
        self.y=y
        
    def Move(self,x,y):
        self.penup()
        self.goto(x,y)
        self.pendown()
        
        
    def Draw(self,color="black"):
        self.Move(self.x,self.y)
        self.dot()
    
    
#Circle 클래스
class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def Draw(self, color="black"):
        self.Move(self.x, self.y - self.radius)
        self.color(color)
        self.begin_fill()
        self.circle(self.radius)
        self.end_fill()


#Rect 클래스
class Rect(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def Draw(self, color="black"):
        self.Move(self.x - self.width / 2, self.y - self.height / 2)
        self.color(color)
        self.begin_fill()
        for i in range(2):
            self.forward(self.width)
            self.right(90)
            self.forward(self.height)
            self.right(90)
        self.end_fill()

# 무작위 도형 생성
def create_random_shape():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    r = random.randint(10, 50)
    w = random.randint(10, 70)
    h = random.randint(10, 70)
    color = random.choice(["red", "green", "blue"])
    shapes = [Shape(x, y), Circle(x, y, r), Rect(x, y, w, h)]
    shape = random.choice(shapes)
    shape.Draw(color)
    return shape

# 무작위 도형 삭제
def delete_random_shape(shapes):
    if len(shapes) > 0:
        index = random.randint(0, len(shapes)-1)
        shape = shapes.pop(index)
        shape.Erase()


def main():
    shapes=[]
    #도형 추가하고 그리기
    shapes.append(Shape(100,200))
    shapes.append(Shape(100,100))
    shapes.append(Shape(100,0))
    for sh in shapes:
        sh.Draw()
        
    #도형 삭제하기
    
    
main()
    