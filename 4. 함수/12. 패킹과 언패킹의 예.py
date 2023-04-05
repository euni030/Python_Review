tuple1 = 1, 2, 3                # 패킹 튜플 : (1, 2, 3)
t1, t2, t3 = (1, 2, 3)          # 언패킹 튜플 : 1, 2, 3
l1, l2, l3 = [11, 12, 13]       # 언패킹 리스트 : 11, 12, 13
d1, d2 = { "cola":100, "cider":50 }   # 딕셔너리 키 언패킹 : "cola", "cider"
s1, s2, s3 = "Ace"              # 언패킹 문자열 : "A", "c", "e"

print(tuple1)
print(t1,t2,t3)
print(l1,l2,l3)
print(d1,d2)
print(s1,s2,s3)