# 별 찍기 - 8
N = int(input())
for i in range(1, N*2):
    if i <= N:
        print('*'*i+' '*2*(N-i)+'*'*i)
    else :
        print('*'*(N*2-i)+' '*2*(i-N)+'*'*(N*2-i))