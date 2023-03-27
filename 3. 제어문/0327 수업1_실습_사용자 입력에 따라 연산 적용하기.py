a,b,op=eval(input("2개의 값과 연산자 입력:")) #1,2,"-"

match op:
    case "+":
        print("f{a} {op} {b}={a+b}")
    case "-":
        print("f{a} {op} {b}={a-b}")
    