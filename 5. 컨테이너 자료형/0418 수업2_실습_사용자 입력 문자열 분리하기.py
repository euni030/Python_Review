a=input("문장을 입력하시오.")
a_list=a.split()

p=print(a_list)

result=0
for i in a_list:
    if i.isnumeric():
        result += eval(i)
print("합산 결과:",result)