def Sum1(x, y, z):
    return x + y + z
print(Sum1(*(1, 2, 3)))     # 1, 2, 3으로 전달
print(Sum1(*[1, 2, 3]))     # 1, 2, 3으로 전달

def Sum2(x, *others):
    return x + sum(others)
print(Sum2(*(1, 2, 3)))     # 1, (2, 3)으로 전달
print(Sum2(*[1, 2, 3]))     # 1, (2, 3)으로 전달
