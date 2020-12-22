# 좌표 정렬하기
def merge_sort(arr_x, arr_y):
    if len(arr_x) < 2 or len(arr_y) < 2:
        return arr_x, arr_y
    mid_x = len(arr_x) // 2
    mid_y = len(arr_y) // 2
    left_x, left_y = merge_sort(arr_x[:mid_x], arr_y[:mid_y])
    right_x, right_y = merge_sort(arr_x[mid_x:], arr_y[mid_y:])
    
    i, j, k = 0, 0, 0

    while i < len(left_x) and j < len(right_x):
        if left_x[i] < right_x[j]:
            arr_x[k] = left_x[i]
            arr_y[k] = left_y[i]
            i += 1
        elif left_x[i] == right_x[j]:
            if left_y[i] < right_y[j]:
                arr_y[k] = left_y[i]
                arr_x[k] = left_x[i]
                i += 1
            else :
                arr_y[k] = right_y[j]
                arr_x[k] = right_x[j]
                j += 1
        else :
            arr_x[k] = right_x[j]
            arr_y[k] = right_y[j]
            j += 1
        k += 1

    while i < len(left_x):
        arr_x[k] = left_x[i]
        arr_y[k] = left_y[i]
        i += 1
        k += 1

    while j < len(right_x):
        arr_x[k] = right_x[j]
        arr_y[k] = right_y[j]
        j += 1
        k += 1
    
    return arr_x, arr_y

N = int(input())
x, y = list(), list()
for _ in range(N):
    a, b = (map(int, input().split()))
    x.append(a)
    y.append(b)

x, y = merge_sort(x, y)

for i, j in zip(x, y):
    print(i, j)