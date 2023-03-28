var = eval(input("데이터 입력 : "))  # 문자열은 'hello'와 같이 입력

match var:
    case int():
        print("정수를 입력하였습니다.")
    case float():
        print("실수를 입력하습니다.")
    case str():
        print("문자열을 입력하였습니다.")
    case list() | tuple():      # 비트 OR 연산(|)을 통해 여러 개 연결 가능
        print("리스트 또는 튜플을 입력하였습니다.")
    case _:
        print("정수, 실수, 문자열, 리스트, 튜플 모두 아닙니다.")
