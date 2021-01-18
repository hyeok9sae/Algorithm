# 랜선 자르기
def binary_search(start, end):
    while start <= end:
        sum = 0
        mid = (start + end) // 2
        for i in lst:
            sum += i // mid
        if sum >= N:
            start = mid + 1
        else:
            end = mid - 1
    return end

K, N = map(int, input().split())
lst = list()
for _ in range(K):
    lst.append(int(input()))
max_lan = max(lst)
print(binary_search(1, max_lan))
