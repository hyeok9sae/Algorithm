# 카드
N = int(input())
cnt = {}
for _ in range(N):
    s = int(input())
    if s in cnt:
        cnt[s] += 1
    else:
        cnt[s] = 1
data = sorted(cnt.items(), key=lambda num: num[0])
data = sorted(data, key=lambda count: count[1], reverse=True)
print(data[0][0])