# 배열 합치기
def mergeSort(lst):
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1
    return lst 

N, M = map(int, input().split())
N_lst = list(map(int, input().split()))
M_lst = list(map(int, input().split()))
N_lst.extend(M_lst)
N_lst = mergeSort(N_lst)
print(*N_lst)

'''
N, M = map(int, input().split())
N_lst = list(map(int, input().split()))
M_lst = list(map(int, input().split()))
N_lst.extend(M_lst)
N_lst = sorted(N_lst)
print(*N_lst)
'''