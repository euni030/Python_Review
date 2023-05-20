class Complex:
    def __init__(self,real,imag):  #실수부 허수부
        self.real=real
        self.imag=imag
        
    def __add__(self, comp):
        return Complex(self.real+comp.real, self.imag+comp.imag)
        
    
    def __str__(self):
        return f"{self.real}+{self.imag}i"

    def __mul__(self,comp):
        return Complex(self.real*comp.real,self.imag*comp.imag)


a=Complex (1,2)
print(a)   #a__str__()로 됨
b=Complex(3,4)
c=a+b  #a__add(b)
print(b)
print(c)
d=a*b