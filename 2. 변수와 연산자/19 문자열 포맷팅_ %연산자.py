x,y=eval(input("정수2개 입력:"))
print("x : %d, y : %d" % (x, y))        # %d : 정수
print("%d" % (16))             # 16
print("%o" % (16))             # 20
print("%x" % (16))             # 10
print("%f" % (123.123))        # 123.123000
print("%e" % (123.123))        # 1.231230e+02
print("%s %s" % ("안녕하세요", 123.123))  #%s이 123.123을 자동으로 str함
# 안녕하세요 123.123
print("%%" % ())               # %