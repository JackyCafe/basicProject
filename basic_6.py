# 熱透選號
import random

s=[]
i = 1
while i <= 6:
    a = random.randint(1, 42)
    if a not in s :
        s.append(a)
        i += 1

a = s.sort()
print(s)