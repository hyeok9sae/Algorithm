# K번째 수
N, K = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
print(lst[K-1])