def RangeSum(m,n,gap=1):
    if m > n:
        m, n = n, m
       
    result=0
    for i in range(m,n+1,gap):
        result+=i
    
    return result
    
    
print(RangeSum(1,5))
print(RangeSum(1,5,2))
print(RangeSum(1,5,3))
