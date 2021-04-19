# 다음 순열
def swap(i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp

def next_perm():
    i = N-1
    while i-1 >= 0 and lst[i-1] > lst[i]:
        i -= 1
    if i-1 < 0:
        return False
    j = N-1
    while j >= 0 and lst[i-1] > lst[j]:
        j -= 1
    swap(i-1, j)
    j = N-1
    while i <= j:
        swap(i, j)
        i += 1
        j -= 1
    return True
    
N = int(input())
lst = list(map(int, input().split()))
if next_perm():
    print(*lst)
else:
    print(-1)