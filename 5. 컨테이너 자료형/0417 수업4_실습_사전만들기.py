#모르겠음;; 왜 결과가 이상하지;;;

data=[]

while 1:
    menu=input("추가, 출력, 종료 입력:")
    if menu=="종료":
        break
    
    if menu=="추가":
        eng, kor=eval(input("영단어와 해설 결과를 입력:"))
        data[eng]=kor

    elif menu=="출력":
        for key in data:
            print(key,":",data[key])
            