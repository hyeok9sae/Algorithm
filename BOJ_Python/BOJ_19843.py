# 수면 패턴
T, N = map(int, input().split())
dic = {'Mon':0,'Tue':1,'Wed':2,'Thu':3,'Fri':4}
sleep = 0
for _ in range(N):
    D1, H1, D2, H2 = map(str, input().split())
    H1, H2 = int(H1), int(H2)
    day = dic[D2]-dic[D1]
    sleep += (day*24)+H2-H1
ans = T-sleep
# print(T, sleep)
if ans > 48:
    print(-1)
elif ans <= 0:
    print(0)
else:
    print(ans)