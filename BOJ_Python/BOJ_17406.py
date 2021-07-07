# 배열 돌리기 4
from itertools import permutations as pm
from copy import deepcopy

def rotate(r, c, s):
    k = 0
    while k < s:
        temp = matrix[r-s+k][c-s+k]
        for i in range(r-s+k, r+s-k):
            matrix[i][c-s+k] = matrix[i+1][c-s+k]
        for i in range(c-s+k, c+s-k):
            matrix[r+s-k][i] = matrix[r+s-k][i+1]
        for i in range(r+s-k, r-s+k, -1):
            matrix[i][c+s-k] = matrix[i-1][c+s-k]
        for i in range(c+s-k, c-s+k+1, -1):
            matrix[r-s+k][i] = matrix[r-s+k][i-1]
        matrix[r-s+k][c-s+k+1] = temp
        k += 1

N, M, K = map(int, input().split())
matrix_one = list(list(map(int, input().split())) for _ in range(N))
rotate_lst = []
for _ in range(K):
    r, c, s = map(int, input().split())
    rotate_lst.append((r, c, s))
rotate_lst = pm(rotate_lst)
answer = float('inf')
for case in rotate_lst:
    matrix = deepcopy(matrix_one)
    for a, b, c in case:
        rotate(a-1, b-1, c)
    res = float('inf')
    for lst in matrix:
        res = min(sum(lst), res)
    if answer > res:
        answer = res
print(answer)