class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def Move(self,x,y):
        self.x +=x
        self.y+=y
    
    def Sum(self,pt):
        return Point(self.x+pt.x, self.y+pt.y)
            
    
    def Print(self):
        print(f"{self.x},{self.y}")
        
        
pt1=Point(1,2)
pt2=Point(3,4)

pt2.Move(100,200)
pt3=pt1.Sum(pt2)

pt1.Print()
pt2.Print()

        