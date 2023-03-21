str1 = input("문자열 입력 : ")

print("str1 : %.5s" % (str1))
print("str1 : %10.5s" % (str1))             # 오른쪽 정렬
print("str1 : {:.5}".format(str1))
print("str1 : {:>10.5}".format(str1))       # 오른쪽 정렬
print(f"str1 : {str1:.5}")
print(f"str1 : {str1:>10.5}")               # 오른쪽 정렬