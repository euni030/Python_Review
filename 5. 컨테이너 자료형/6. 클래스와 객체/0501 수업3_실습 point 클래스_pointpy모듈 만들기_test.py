from point import Point

pt1=Point(1,2)
pt2=Point(3,4)
pt3=pt1*10
pt4=-10*pt2

print(pt1)
print(pt2)
print(pt3)
print(pt4)

if pt1<pt2:
    print("pt1이 pt2보다 더 작습니다.")
elif pt1>pt2:
    print("pt1이 pt2보다 더 큽니다.")
else: 
    print("pt1과 pt2는 같습니다.")