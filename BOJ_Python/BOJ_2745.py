# 진법 변환
N, B = map(str, input().split())
N = list(N)
ans = 0
for i in range(len(N)-1, -1, -1):
    j = N.pop(0)
    if "A" <= j <= "Z":
        ans += (ord(j)-55)*(int(B)**i)
    else:
        ans += int(j)*(int(B)**i)
print(ans)