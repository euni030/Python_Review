var=eval(input("튜플 좌표(x,y)입력:"))

match var:
    case(0,0):
        print("(0,0):원점")
    case(0,y):
        print(f"(0,{y}): x좌표 0")
    case(x,0):
        print(f"({x},0): y좌표 0")
    case(x,y):
        print(f"({x},{y}): x,y 모두 0이 아님")
    case _:
        print("좌표 입력 오류")
        