class circle:
    def __init__(self,x,y,r=1):
        self.x=x
        self.y=y
        self.r=r
        
    def GetArea(self):
        return 3.14*self.r**2
    
    def Move (self,x,y):
        self.x+=x
        self.y+=y
    
    def __str__(self):
        print(f"중심:{self.x, self.y}\n반지름 : {self.r}\n면적:{self.GetArea()}")
    

cir1= circle(1,2,3)
print(cir1.GetArea())
cir1.Move(100,200)
cir1.__str__()   #중심 좌표, 반지름, 면접 출력

# cir_list=[]
# for i in range(10):
#     cir_list.append(circle())