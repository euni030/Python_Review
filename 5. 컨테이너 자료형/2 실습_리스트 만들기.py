import random

list_a=[num for num in range(1,101) if num%3==0 and num%5==0]
print(list_a)

list_b=[random.randint(1,10) for i in range(10)]
print(list_b)

directions=['동','서','남','북']
list_c=[random.choice(directions) for i in range(10)]
print(list_c)