# 수 정렬하기 3
import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
lst = [0]*10001
for _ in range(N):
    k = int(input())
    lst[k] += 1

for i in range(len(lst)):
    if lst[i] == 0:
        continue
    for _ in range(lst[i]):
        print(str(i)+'\n')
