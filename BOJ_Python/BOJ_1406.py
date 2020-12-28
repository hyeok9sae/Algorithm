# 에디터
import sys
input = sys.stdin.readline
from collections import deque
# print = sys.stdout.write
class Editor:
    def __init__(self, s):
        self.lst = deque()
        self.lst.extend(s)
        self.cursor = len(self.lst)-1
    def L(self):
        if self.cursor == -1:
            return
        self.cursor -= 1
    def D(self):
        if self.cursor == len(self.lst)-1:
            return
        self.cursor += 1
    def B(self):
        if self.cursor == -1:
            return
        self.lst.pop(self.cursor)
        self.cursor -= 1
    def P(self, S):
        self.lst.insert(self.cursor+1, S)
        self.cursor += 1

s = input().strip()
n = int(input())
ed = Editor(s)
for _ in range(n):
    msg = input().split()
    if msg[0] == 'L':
        ed.L()
    if msg[0] == 'D':
        ed.D()
    if msg[0] == 'B':
        ed.B()
    if msg[0] == 'P':
        ed.P(msg[1])

for i in ed.lst:
    print(i, end='')