# 별 찍기 - 9
N = int(input())
for i in range(1, N*2):
    if i <= N:
        print(' '*(i-1)+'*'*((N-i)*2+1))
    else:
        print(' '*(N*2-i-1)+'*'*((i-N)*2+1))