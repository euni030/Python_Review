list1=[1,2,3,4,5]    #변경 가능 객체
int1=1000            #변경 불가능 객체
print("list1 객체의 id:",id(list1),"값:",list1)
print("int1 객체의 id:",id(int1),"값:",int1)

list1[0]=100         #변경 가능 객체: 요소 값이 변경됨
int1=2000            #변경 불가능 객체: 객체가 변경됨
print("list1 객체의 id:",id(list1),"값:",list1)
print("list1 객체의 id:",id(int1),"값:",int1)

list1=[-1,-2,-3]     #변경 가능 객체: 리스트 전체를 변경하면 객체가 변경됨
print("list1 객체의 id:", id(list1),"값:",list1)



