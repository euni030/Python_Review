var1=3
print(id(var1))
var2=1.2
var3=3
print(id(var3))   #id(var1)와 동일

del(var3)   #변수 무효화 --> del 연산자   del(var1)또는 del var1

print(var1)
print(var3)  #에러