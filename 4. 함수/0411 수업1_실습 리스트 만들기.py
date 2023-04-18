data1=[]
for i in range(1,100):
    if i%3==0 and i%5==0:
        data1.append(i)
print(data1)

import random

data2=[]
for i in range(10):
   data2.append(random.randint(1,10))
    
print(data2)

data3=[]
for i in range(10):
    data3.append(random.choice(['동','서','남','북']))
print(data3)
