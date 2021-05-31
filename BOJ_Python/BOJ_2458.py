# 키 순서
from collections import deque

def bfs(num):
    visited[num] = True
    deq = deque([num])
    while deq:
        number = deq.popleft()
        for i in dic[number]:
            if visited[i]:
                continue
            visited[i] = True
            deq.append(i)

N, M = map(int, input().split())
dic = {}
for i in range(1, N+1):
    dic[i] = []
for _ in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
ans = 0
for i in range(1, N+1):
    flag = False
    visited = [False]*(N+1)
    bfs(i)
    for j in range(1, len(visited)):
        if not visited[j]:
            flag = True
            break
    print(visited)
    if not flag:
        ans += 1
print(ans)