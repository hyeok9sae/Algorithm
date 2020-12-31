# 소수 찾기
N = int(input())
lst = list(map(int, input().split(' ')))
for i in lst:
    if i == 1:
        N -= 1
    for j in range(2, i):
        if i%j == 0:
            N -= 1 
            break
print(N)