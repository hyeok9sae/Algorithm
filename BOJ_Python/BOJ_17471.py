# 게리맨더링
from itertools import combinations as cb
from collections import deque

def bfs(lst):
    visited[lst[0]] = True
    deq = deque()
    deq.append(lst[0])
    cnt, sum = 0, 0
    while deq:
        v = deq.popleft()
        cnt += 1
        sum += person[v]
        for idx, i in enumerate(matrix[v]):
            if i == 0 or visited[idx]:
                continue
            if idx not in lst:
                continue
            visited[idx] = True
            deq.append(idx)
    return cnt, sum

N = int(input())
person = [0] + list(map(int, input().split()))
matrix = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    lst = list(map(int, input().split()))
    for j in lst[1:]:
        matrix[i][j] = matrix[j][i] = 1
answer = float('inf')
for i in range(1, N):
    combis = cb(range(1, N+1), i)
    for combi in combis:
        visited = [False]*(N+1)
        cnt_a, sum_a = bfs(combi)
        temp = []
        for i in range(1, N+1):
            if i not in combi:
                temp.append(i)
        cnt_b, sum_b = bfs(temp)
        if cnt_a+cnt_b == N:
            answer = min(abs(sum_a-sum_b), answer)
print(answer if answer != float('inf') else -1)