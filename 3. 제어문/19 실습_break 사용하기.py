n=int(input("2이상의 자연수 하나(n)를 입력하라:"))
i=1
result=0

while True:
    result+=i
    
    if n<result:
        break
    i+=1

print(n,"을 넘지 않는 1+...+i의 가장 큰 i 값은 ",i-1,"이고, 그때 합산 결과는 ",result-i," 입니다.") 