# x부터 y까지 합산한 결과 반환
def Sum(x, y):
    return Sum(range(x, y + 1))

for i in [1, 2]:
    for j in [10, 20]:
        print((lambda x=i, y=j: Sum(x, y))())       # 매개변수 디폴트 값
        # print((lambda: Sum(i, j))())
        # print((lambda x, y: Sum(x, y))(i, j))
