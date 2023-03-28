num1,num2=eval(input("2개의 정수 입력:"))
result=0

for i in range(num1,num2+1):
    result+=i
print("합계:",result)   