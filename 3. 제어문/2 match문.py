var=input("가위, 바위,보 입력:")

match var:
    case "가위":
        print("가위를 냈습니다.")
    case "바위":
        print("바위를 냈습니다.")
    case "보":
        print("보를 냈습니다.")
    case _:
        print("입력 오류입니다.")
        
        