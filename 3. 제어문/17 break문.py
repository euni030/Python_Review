result=0
i=1

while True:  #break문이 없다면 무한 루프가 됨
    if i ==11:   #i 값이 11이 되면
        break    #while루프를 빠져나감
    result+=i
    i+=1
    
print(result)