x = eval(input("실수 입력 : "))

print("x : %.2f" % (x))           # 소수점 이하 2자리
print("x : %10.2f" % (x))         # 오른쪽 정렬
print("x : {:.2f}".format(x))     # 소수점 이하 2자리
print("x : {:>10.2f}".format(x))  # 오른쪽 정렬
print("x : {0:.6}".format(x))     # 전체 6자리
print("x : {}".format(x))         # 원래 그대로
print(f"x : {x:.2f}")             # 소수점 이하 2자리
print(f"x : {x:>10.2f}")          # 오른쪽 정렬
print(f"x : {x}")                 # 원래 값 그대로
