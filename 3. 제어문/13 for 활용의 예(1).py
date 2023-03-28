result=0
for num in [1,2,3,4,5,6,7,8,9,10]:   #리스트 사용
    result+=num
print(result)

result=0
for num in range(1,11):   #range사용
    result+=num
print(result)

result=0
for num in list(range(1,11)):   #range를 리스트로 변환
    result+=num
print(result)
