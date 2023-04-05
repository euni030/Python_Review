def Print(msg, count):
    for i in range(count):
        print(msg)
        
message,n=eval(input("메세지와 출력횟수 입력:"))
Print(message, n)