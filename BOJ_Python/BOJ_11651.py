# 좌표 정렬하기 2
N = int(input())
lst = list()
for _ in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))

lst = sorted(lst, key=lambda x:x[0])
lst = sorted(lst, key=lambda y:y[1])
for i, j in lst:
    print(i, j)