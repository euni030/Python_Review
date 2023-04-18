start,end,gap=eval(input("시작, 끝, 가격 입력:"))
A=set(range(start,end+1,gap))

start,end,gap=eval(input("시작, 끝, 가격 입력:"))
B=set(range(start,end+1,gap))

    

print(A |B)
print(A&B)
