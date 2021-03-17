# 약수의 합
T = int(input())
d = [1]*1000001
s = [1]*1000001
for i in range(2, 1000001):
    j = 1
    while i*j < 1000001:
        d[i*j] += i
        j += 1
for i in range(2, 1000001):
    s[i] = s[i-1] + d[i]
ans = []
for _ in range(T):
    N = int(input())
    ans.append(s[N])
print(*ans, sep="\n")