data=[]   #빈 리스트
for i in range(5):
    data.append(i*i)  #0, 1, 4, 9, 16

data[0]=3.4

for i in data:
    print(f"{i} ", end='')
print()

for i in range(len(data)):
   print(f"[{i}]:{data[i]}", end=" ")