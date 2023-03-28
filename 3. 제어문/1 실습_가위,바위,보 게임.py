import random
user=input("가위, 바위, 보 중에 하나를 입력:")
computer=random.choice(['가위','바위','보'])

print("당신은 ",user,"을 냈습니다.")
print("컴퓨터는 ",computer,"을 냈습니다.")

# 결과 판정
if user == computer:
    print("비겼습니다!")
elif user == "가위" and computer == "보":
    print("사용자 승리!")
elif user == "바위" and computer == "가위":
    print("사용자 승리!")
elif user == "보" and computer == "바위":
    print("사용자 승리!")
else:
    print("컴퓨터 승리!")
