# 텀 프로젝트
import sys
# 백준에서 pypy3로 재귀호출리미트를 늘려주는 코드를 작성하지 않으면 런타임에러 발생
sys.setrecursionlimit(111111)

def dfs(V):
    if check[V] == 2 or check[V] == -1:
        return
    check[V] += 1
    if check[lst[V]] != 2:
        dfs(lst[V])
    if check[V] < 2:
        check[V] = -1
    return

T = int(input())
for _ in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.insert(0, 0)
    check = [0]*(n+1)
    for i in range(1, n+1):
        if check[i] == 0:
            dfs(i)
    print(check.count(-1))