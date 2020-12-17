# 별 찍기 - 4
N = int(input())
for i in range(1, N+1):
    print(' '*(i-1)+'*'*(N-i+1))