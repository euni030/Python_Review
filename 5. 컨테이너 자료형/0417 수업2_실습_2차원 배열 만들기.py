import random
data=[]
row,col=eval(input("행, 열 개수 입력:"))

for i in range(row):
    data.append([])
    for j in range(col):
        data[i].append(random.randint(1,100))
        


print(data)