# 날짜 계산
E, S, M = map(int, input().split())
E -= 1
S -= 1
M -= 1
cnt = 0
while True:
    if cnt%15 == E and cnt%28 == S and cnt%19 == M:
        break
    cnt += 1
print(cnt+1)