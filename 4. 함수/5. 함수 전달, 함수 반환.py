def HelloMethod1():
    print("Hello!!!")

def HelloMethod2():
    print("안녕하세요~~~")

def SayHello(hello1, hello2):
    hello1()               # hello1으로 전달된 함수가 실행됨
    return hello2          # hello2로 전달된 함수가 반환됨

reply = SayHello(HelloMethod1, HelloMethod2)    # reply는 HelloMethod2 참조
reply()                    # HelloMethod2 실행
