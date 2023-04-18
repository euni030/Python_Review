def FilterFunc(num):
   #return True if num%3==0 else Flase    이렇게 쓸 수도 있다
   if num%3==0:
       return True
   else:
       return False


def MapFunc(num):
    return num**2
    

def Func(data):
    data2=list(filter(FilterFunc,data))
    data3=list(map(MapFunc,data2))
    return data3

print(Func([1,2,3,4,5,6,7,8,9,10])) #[3,6,9]->[9,36,8]