import random       # random 모듈 import

# 주사위 눈의 값들 중 하나를 생성한다.
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print("첫 번째 주사위의 값:",dice1)
print("두 번째 주사위의 값:",dice2)

print("합산 결과:",dice1+dice2)
