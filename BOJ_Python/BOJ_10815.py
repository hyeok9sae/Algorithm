# 숫자 카드
def binary_search(start, end, num):
    while start <= end:
        mid = (start + end) // 2
        if num > num_lst[mid]:
            start = mid + 1
        elif num == num_lst[mid]:
            return 1
        else:
            end = mid - 1
    return 0

N = int(input())
num_lst = sorted(list(map(int, input().split())))
M = int(input())
find_lst = list(map(int, input().split()))
for i in find_lst:
    print(binary_search(0, len(num_lst)-1, i), end=" ")