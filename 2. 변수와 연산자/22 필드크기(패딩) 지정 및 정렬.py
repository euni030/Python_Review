x, y = eval(input("정수 2개 입력 : "))

print("x : %-6d, y : %6d" % (x, y))             # x 왼쪽 정렬, y 오른쪽 정렬
print("x : {0:<6d}, y : {1:>6d}".format(x, y))
print(f"x : {x:<6d}, y : {y:>6d}")

print("x : {0:*<6d}, y : {1:*>6d}".format(x, y))    # 공백 위치에 * 문자 출력
print(f"x : {x:*<6d}, y : {y:*>6d}")
