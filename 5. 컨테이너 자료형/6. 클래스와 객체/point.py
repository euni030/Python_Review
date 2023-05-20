class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __mul__(self,val):
        return Point(self.x * val, self.y * val)

    def __rmul__(self,val):
        return Point(self.x * val, self.y * val)
        
    def __lt__(self,pt):
        return(self.x + self.y)<(pt.x+pt.y)
    
    def __gt__(self,pt):
        return(self.x + self.y)>(pt.x+pt.y)
     
    def __str__(self):
        return f"({self.x}, {self.y})"

