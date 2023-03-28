result = 0

for i in range(1, 5):
    if i % 3 == 0:      # 3의 배수라면
        continue        # skip(코드 블록 내 이후 코드를 실행하지 않고 바로 반복문의 시작 위치로 이동)
    result += i

print(result)
