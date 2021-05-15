# 최댓값
max, max_cnt = 0, 0
cnt = 0
for _ in range(9):
    N = int(input())
    cnt += 1
    if max < N:
        max = N
        max_cnt = cnt
print(max, max_cnt, sep="\n")