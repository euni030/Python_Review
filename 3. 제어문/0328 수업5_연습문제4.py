num=int(input("2 이상의 자연수 1개 입력:"))

prime=True

for i in range(2,num):
    if num%1==0:
        prime=False
        break

if prime:
    print("소수")
else:
    print("소수가 아니다.")