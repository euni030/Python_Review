def Change(method, data):   # 리스트 data의 값들을 method 함수에 따라 변환
    new_data = []
    for num in data:
        new_data.append(method(num))
    return new_data

values = [1, 2, 3, 4, 5]
print(Change(lambda x: x ** 2, values))    # [1, 4, 9, 16, 25]
print(Change(lambda x: x + x, values))     # [2, 4, 6, 8, 10]
