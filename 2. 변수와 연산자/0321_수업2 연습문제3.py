import random

dice1=random.uniform(1,100)
dice2=random.uniform(1,100)

print(f"{dice1:.2f}+{dice2:.2f}={dice1+dice2:.2f}")
print(f"{dice1:.2f}&{dice2:.2f}={int(dice1)&int(dice2):.2f}")
