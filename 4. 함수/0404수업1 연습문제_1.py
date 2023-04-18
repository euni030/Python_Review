#참고! 진약수: 자신을 포함 안한거ㅇㅇ
#진약수의 합을 반환
def SumOfProperDivisor(n):
    result=0
    for i in range(1,n):
        if n%i==0:
            result +=i
    return result 
    
#약수의 합을 반환
def SumOfDivisor(n):
   return SumOfProperDivisor(n)+n
    
    
    
    
print("6  의 약수의	합	:" , SumOfDivisor(6))
print("6  의 진약수의	합	:" , SumOfProperDivisor(6))
print("9 의	약수의	합	:"  , SumOfDivisor(9))
print("9 의	진약수의 	합	:" , SumOfProperDivisor(9))
 