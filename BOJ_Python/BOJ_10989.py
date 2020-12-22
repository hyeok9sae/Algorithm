# 수 정렬하기 3
N = int(input())
lst = list()
for _ in range(N):
    lst.append(int(input()))
lst = sorted(lst)
for i in lst:
    print(i)
