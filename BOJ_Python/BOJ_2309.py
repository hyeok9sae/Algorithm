# 일곱 난쟁이
from itertools import permutations as perm
lst, ans = [], []
for _ in range(9):
    lst.append(int(input()))

for i in perm(lst, 7):
    if sum(i) == 100:
        for j in i:
            ans.append(j)
        break
ans.sort()
print(*ans, sep='\n')