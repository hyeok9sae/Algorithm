# 약수
N = int(input())
lst = [*map(int, input().split())]
lst.sort()
print(lst[0]*lst[-1])