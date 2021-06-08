# 뮤탈리스크
from itertools import permutations as pm
from collections import deque

def check(tmp):
    for i in tmp:
        if i > 0:
            return False
    return True

def destroy():
    deq = deque()
    visited[scv[0]][scv[1]][scv[2]] = True
    deq.append((scv, 0))
    while deq:
        tmp, cnt = deq.popleft()
        if check(tmp):
            return cnt
        for m in mutal:
            lst = []
            for i in range(3):
                if tmp[i]-m[i] < 0:
                    lst.append(0)
                    continue
                lst.append(tmp[i]-m[i])
            if visited[lst[0]][lst[1]][lst[2]]:
                continue
            visited[lst[0]][lst[1]][lst[2]] = True
            deq.append((lst, cnt+1))

N = int(input())
scv = [*map(int, input().split())]
if len(scv) == 1:
    scv.append(0)
    scv.append(0)
elif len(scv) == 2:
    scv.append(0)
mutal = list(pm([9,3,1]))
visited = [[[False]*61 for _ in range(61)] for _ in range(61)]
# print(visited)
print(destroy())