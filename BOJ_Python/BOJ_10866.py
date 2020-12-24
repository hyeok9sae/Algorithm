# 덱
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
deq = deque()
for _ in range(N):
    msg = input().strip().split()
    if msg[0] == 'push_front':
        deq.appendleft(msg[1])
    if msg[0] == 'push_back':
        deq.append(msg[1])
    if msg[0] == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:    
            print(deq.popleft())
    if msg[0] == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    if msg[0] == 'size':
        print(len(deq))
    if msg[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    if msg[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    if msg[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])