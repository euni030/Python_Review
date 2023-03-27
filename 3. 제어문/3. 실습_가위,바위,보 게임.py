import random
user=input("가위, 바위, 보 중에 하나를 입력:")
computer=random.choice(['가위','바위','보'])

print("당신은 ",user,"을 냈습니다.")
print("컴퓨터는 ",computer,"을 냈습니다.")

if user==computer:
    print("비겼습니다")
elif user== '가위':
    if computer=='바위':
        print("컴퓨터가 이겼습니다.")
    else computer=='보':
        print("당신이 이겼습니다.")
elif user=='바위':
    
else :#user=='보'
    
