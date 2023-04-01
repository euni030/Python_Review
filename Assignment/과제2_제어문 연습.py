import random

num=int((input(">가위,바위,보 게임을 몇 회 실시하겠습니까?")))
while(num<6):
    num = int((input(">가위,바위,보 게임을 몇 회 실시하겠습니까?")))
print("=============================================")



win_computer=0
same=0
win_user=0

for i in range(1,num+1):
    print(">",i,"회차 게임을 시작합니다.")
    user=input("가위,바위,보를 선택하세오:")
    computer = random.choice(['가위', '바위', '보'])
    print("컴퓨터는" , computer , "을(를) 냈습니다.")

    if user==computer:
        print("*비겼습니다.")
        same+=1
    elif (user=="가위" and computer=="바위")|(user=="바위" and computer=="보")|(user=="보" and computer=="가위"):
        print("*컴퓨터가 이겼습니다.")
        win_computer+=1
    else:
        print("*축하합니다. 당신이 이겼습니다.")
        win_user+=1

print("=============================================")
print(">>> 게임이 종료되었습니다")
print("컴퓨터가 이긴 횟수:",win_computer)
print("비긴 횟수:",same)
print("당신이 이긴 횟수:",win_user)