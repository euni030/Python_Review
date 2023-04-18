data=[]

while 1:
    menu=input("추가, 삭제, 종료 입력:")
    if menu =="종료":
        break
    
    if menu=="추가":
        index, value=eval(input("추가 위치와 값을 입력:"))
        data.insert(index,value)
        print(data)
        
        
        #이상하게 한듯 확인 다시하기.
    if menu=="삭제":
        index=input("삭제할 위치를 입력: ")
        data.pop(index)
        print(data)