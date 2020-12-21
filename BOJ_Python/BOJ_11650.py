# 좌표 정렬하기
N = int(input())
x, y = list(), list()
for _ in range(N):
    x, y.append(map(int, input().split()))

print(x, y)