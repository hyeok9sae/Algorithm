# 톱니바퀴 (2)
# import copy

def rotate(num, dir):
    if visited[num]:
        return 
    visited[num] = True
    if dir == -1:
        if num+1 <= T-1 and matrix[num][2] != matrix[num+1][6]:
            rotate(num+1, 1)
        if num-1 >= 0 and matrix[num][6] != matrix[num-1][2]:
            rotate(num-1, 1)
        tmp = matrix[num][0]
        for i in range(1, 8):
            matrix[num][i-1] = matrix[num][i]
        matrix[num][7] = tmp
    elif dir == 1:
        if num+1 <= T-1 and matrix[num][2] != matrix[num+1][6]:
            rotate(num+1, -1)
        if num-1 >= 0 and matrix[num][6] != matrix[num-1][2]:
            rotate(num-1, -1)
        tmp = matrix[num][7]
        for i in range(7, 0, -1):
            matrix[num][i] = matrix[num][i-1]
        matrix[num][0] = tmp

T = int(input())
matrix = []
for _ in range(T):
    matrix.append(list(map(int, input())))
K = int(input())
for _ in range(K):
    visited = [False]*T
    number, direction = map(int, input().split())
    # matrix = copy.deepcopy(lst)
    rotate(number-1, direction)
    # lst = matrix
    # print(*lst, sep="\n")
ans = 0
# print(*lst, sep="\n")
for i in range(T):
    if matrix[i][0] == 1:
        ans += 1
print(ans)