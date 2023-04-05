def GetArea(radius):            # radius : 지역 변수
    area = 3.14 * radius ** 2   # area : 지역 변수
    return area

result = GetArea(1)             # result : 전역 변수
#print(f"면적 : {area})         # 에러 : area는 GetArea 함수의 지역 변수
print(f"면적 : {result}")
