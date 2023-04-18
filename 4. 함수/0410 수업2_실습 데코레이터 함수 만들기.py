def Hello(func):
    def DecoFunc():
        x,y=eval(input("숫자 2개 입력:"))
        result=func(x,y)
        print("계산 결과:",result)
    return DecoFunc
        
        
@Hello
def Sum(x,y):
    return x+y
    return x+y

@Hello
def Sub(x,y):
    return x-y

Sum()
Sub()