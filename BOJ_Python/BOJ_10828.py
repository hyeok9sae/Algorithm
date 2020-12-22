# 스택
import sys
input = sys.stdin.readline
class Stack:
    def __init__(self):
        self.stack = list()
    
    def push(self, X):
        self.stack.append(X)
    
    def pop(self):
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)

    def empty(self):
        if len(self.stack) == 0:
            return 1
        return 0
    
    def top(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

N = int(input())
stack = Stack()
for _ in range(N):
    msg = input().split()
    if msg[0] == 'push':
        stack.push(int(msg[1]))
    elif msg[0] == 'pop':
        print(stack.pop())
    elif msg[0] == 'size':
        print(stack.size())
    elif msg[0] == 'empty':
        print(stack.empty())
    else:
        print(stack.top())
'''
import sys
input = sys.stdin.readline

N = int(input())
stack = list()
for _ in range(N):
    msg = input().split()
    if msg[0] == 'push':
        stack.append(msg[1])
    elif msg[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif msg[0] == 'size':
        print(len(stack))
    elif msg[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
'''