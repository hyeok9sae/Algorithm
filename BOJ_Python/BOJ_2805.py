# 나무 자르기
def binary_search(start, end):
    while start <= end:
        wood = 0
        mid = (start + end) // 2
        for i in lst:
            if i - mid < 0:
                continue
            wood += i - mid
        if wood >= M:
            start = mid + 1
        else:
            end = mid - 1
    return end

N, M = map(int, input().split())
lst = list(map(int, input().split()))
print(binary_search(1, max(lst)))
