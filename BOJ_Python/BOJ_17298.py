# 오큰수
from collections import deque

ans = deque()
N = int(input())
lst = list(map(int, input().split()))
stack = []
for i in range(len(lst)-1, -1, -1):
    while True:
        if len(stack) == 0:
            ans.appendleft(-1)
            stack.append(lst[i])
            break
        if lst[i] < stack[-1]:
            ans.appendleft(stack[-1])
            stack.append(lst[i])
            break
        else:
            stack.pop()
print(*ans)