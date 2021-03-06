# 스타트와 링크
def solve(idx, first, second):
    if len(first) == N/2 and len(second) == N/2:
        res_first, res_second = 0, 0
        for i in range(len(first)):
            for j in range(len(first)):
                if i == j:
                    continue
                res_first += matrix[first[i]][first[j]]
                res_second += matrix[second[i]][second[j]]
        res = abs(res_first-res_second)
        global min
        if min > res:
            min = res
        # return
    if idx == N:
        # print(first, second)
        return
    solve(idx+1, first+[idx], second)
    solve(idx+1, first, second+[idx])

N = int(input())
matrix = [[*map(int, input().split())] for _ in range(N)]
first, second = [], []
min = float('inf')
solve(0, first, second)
print(min)