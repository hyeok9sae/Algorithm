# 리모컨
def check(num):
    if num == 0:
        if visited[num]:
            return 0
        else:
            return 1
    else:
        length = 0
        while num > 0:
            if visited[num%10]:
                return 0
            else:
                length += 1
                num//=10
        return length

N = int(input())
M = int(input())
visited = [False]*10
if M > 0:
    broken = list(map(int, input().split()))
else:
    broken = []
for i in broken:
    visited[i] = True
ans = abs(N-100)
for i in range(1000000+1):
    size = check(i)
    if size > 0:
        res = abs(i-N)
        if ans > size + res:
            ans = size + res
print(ans)