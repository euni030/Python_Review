def Sum1(*nums):         # 튜플 nums로 전달된 모든 값들을 합산하기
    return sum(nums)

print(Sum1(1, 2, 3))                         # 6
print(Sum1(1, 2, 3, 4, 5))                   # 15
print(Sum1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))   # 55

def Sum2(first, *nums):  # 첫 번째를 제외하고 nums의 모든 값들 합산하기
    print(nums)
    return sum(nums)

print(Sum2(1, 2, 3))                         # 5
print(Sum2(1, 2, 3, 4, 5))                   # 14
print(Sum2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))   # 54
