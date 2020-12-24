# 큐
import sys
input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.queue = list()
    
    def push(self, X):
        self.queue.append(X)
    
    def pop(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def empty(self):
        if len(self.queue) == 0:
            return 1
        return 0

    def front(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[0]
    
    def back(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]

N = int(input())
queue = Queue()
for _ in range(N):
    msg = input().strip().split()
    if msg[0] == 'push':
        queue.push(msg[1])
    elif msg[0] == 'pop':
        print(queue.pop())
    elif msg[0] == 'size':
        print(queue.size())
    elif msg[0] == 'empty':
        print(queue.empty())
    elif msg[0] == 'front':
        print(queue.front())
    else:
        print(queue.back())