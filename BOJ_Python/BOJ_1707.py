# 이분 그래프
from collections import deque

def bfs(num):
    visited[num] = True
    flag[num] = True
    deq = deque()
    deq.append(num)
    while deq:
        d = deq.popleft()
        for i in matrix[d]:
            if not visited[i]:
                visited[i] = True
                deq.append(i)
                flag[i] = not flag[d]
            if visited[i]:
                if flag[i] == flag[d]:
                    return False
    return True

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    matrix = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    flag = [False for _ in range(V+1)]
    check = False
    for _ in range(E):
        v1, v2 = map(int, input().split())
        matrix[v1].append(v2)
        matrix[v2].append(v1)
    # 연결그래프인지 비연결그래프인지도 판별해야하므로 모든 정점에서 확인해야함
    for i in range(1, V+1):
        if not visited[i]:
            if not bfs(i):
                check = True
                break
    if check:
        print("NO")
    else:
        print("YES")
