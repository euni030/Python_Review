var1=()
var2=(1,2,3)
var3=(1,3.4,[100,200],{"홍길동":100,"이순신":95})
#var3[2][0]=100     #불가능->에러 발생
var3[2][0]=10000

print(var1);print(var2);print(var3)