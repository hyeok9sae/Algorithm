# 2진수 8진수
print(oct(int(input(), 2))[2:])
''' 시간초과
import sys
input = sys.stdin.readline
print = sys.stdout.write
N = list(input().strip())
num10 = 0
num8 = ""
for i in range(len(N)):
    num = int(N.pop())
    if num == 0:
        continue
    num10 += 2**i
while num10 > 0:
    num8 += str(num10%8)
    num10 //= 8
print(num8[::-1])
'''    