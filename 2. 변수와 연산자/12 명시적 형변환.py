var1=12.345
var2=int(var1)  #12.345가 float에서 int로 변환 되어 12가 됨. (데이터 손실 발생)
var3=float("12.345")   #str타입인 "12.345"가 float타입인 12.345로 변환됨

print("var2:", var2)
print("var3:", var3)