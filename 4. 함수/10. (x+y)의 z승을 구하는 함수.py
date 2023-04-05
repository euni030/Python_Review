def PowerOfSum(x, y, z):
    return (x + y) ** z

print(PowerOfSum(2, 3, 4))                 # 위치 인수
print(PowerOfSum(y = 3, z = 4, x = 2))     # 키워드 인수
print(PowerOfSum(2, z = 4, y = 3))         # mixed 위치 & 키워드 인수
#PowerOfSum(x = 2, 3, 4)                   # 에러
