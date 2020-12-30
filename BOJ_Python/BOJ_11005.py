# 진법 변환 2
N, B = map(int, input().split())
ans = list()
while N > 0:
    if N%B > 9:
        ans.append(chr(N%B+55))
    else:
        ans.append(str(N%B))
    N //= B
for _ in range(len(ans)):
    print(ans.pop(), end="")