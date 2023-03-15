#complex  ---> (실수부 + 허수부i)의 복소수 표현
comp1 = complex(1, 1)               # 1 + 1j
comp2 = complex(1, -1)              # 1 - 1j

print(comp1 + comp2)
print(comp1 - comp2)
print(comp1 * comp2)
print(comp1 / comp2)
print(comp1.real, comp1.imag)       # 실수부, 허수부
