def Print(x, y):
    print(x,"+",y,"=",x+y)
    print(f"{x}-{y}={x-y}")
    print(x,"*",y,"=",x*y) 
    if y==0:
        print("나누기 불가")
    else:
        print(f"{x}/{y}={x-y}")

x2,y2=eval(input("2개의 숫자 입력:"))
Print(x2,y2)
    