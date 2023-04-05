def Sum(x, y):
    result = 0
    if y < x:
        x, y = y, x  # 작은 값을 x로, 큰 값을 y로 대입

    for i in range(x, y + 1):
        result += i

    return result       # 합산 결과 반환

print(Sum(10, 1))
num = Sum(20, 30)   # 반환값을 변수에 대입하여 사용 가능
print(num)
