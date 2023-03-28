import random       # random 모듈 import

# 주사위 눈의 값들 중 하나를 생성한다.
dice = random.randint(1, 6)
print(dice)

# 100과 200 사이의 값들 중 짝수 하나를 생성한다.
even = random.randrange(100, 201, 2)
print(even)

# 0과 1 사이 실수값 중 하나를 생성한다. 
front = random.random()                 
print(front)

# "가위", "바위", "보" 중에 하나를 생성한다.
com = random.choice(["가위", "바위", "보"])
print(com)

# card([1, 2, 3, 4, 5])를 무작위로 섞는다.
card = [1, 2, 3, 4, 5]
random.shuffle(card)
print(card)