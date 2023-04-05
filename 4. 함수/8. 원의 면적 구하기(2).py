def GetArea():
    global area                 # 전역 변수 area 의미 => 읽기/쓰기 모두 가능
    area = 3.14 * radius ** 2   # 전역 변수 radius => 읽기 가능, 쓰기 불가능

radius = 1
area = None
GetArea()
print(f"면적 : {area}")
