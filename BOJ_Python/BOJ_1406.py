# 에디터
from collections import deque
deq1, deq2 = deque(), deque()
inp = input()
for i in inp:
    deq1.append(i)
N = int(input())
for _ in range(N):
    msg = list(input().split())
    if msg[0] == "L":
        if len(deq1) == 0:
            continue
        deq2.appendleft(deq1.pop())
    if msg[0] == "D":
        if len(deq2) == 0:
            continue
        deq1.append(deq2.popleft())
    if msg[0] == "B":
        if len(deq1) == 0:
            continue
        deq1.pop()
    if msg[0] == "P":
        deq1.append(msg[1])
deq1 += deq2
# print(''.join(deq1))
print(''.join(deq1))