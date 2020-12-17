# 별 찍기 - 17
N = int(input())
for i in range(1, N+1):
    if i == N:
        print('*'*(N*2-1))
        break
    if i == 1:
        print(' '*(N-i)+'*')
        continue
    print(' '*(N-i)+'*'+' '*(i*2-3)+'*')