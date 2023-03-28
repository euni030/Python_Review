var = int(input("자연수 입력 : "))

if var % 2 == 0:
    print(var, ":", "짝수")
else:
    print(var, ":", "홀수")

print(var,":","짝수") if var%2==0 else print(var,":","홀수")  #예시1
print(var,":","짝수"if var%2==0 else"홀수")