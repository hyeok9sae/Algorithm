# 수 찾기
def binary_search(number):
    start, end = 0, N-1
    while start <= end:
        mid = (start+end)//2
        if number < A[mid]:
            end = mid-1
        elif number > A[mid]:
            start = mid+1
        else:
            return True
    return False

N = int(input())
A = list(map(int, input().split()))
A.sort()
# print(A)
M = int(input())
B = list(map(int, input().split()))
for i in B:
    if binary_search(i):
        print(1)
    else:
        print(0)