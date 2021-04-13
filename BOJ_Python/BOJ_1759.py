# 암호 만들기
def comb(n, r):
    if r == 0:
        print(*tmp, sep=" ")
        return
    for i in range(n):
        if not visited[i]:
            tmp.append(lst[i])
            visited[i] = True
            comb(n, r-1)
            tmp.pop()
            visited[i] = False

L, C = map(int, input().split())
lst = list(map(str, input().split()))
vowel = ['a', 'e', 'i', 'o', 'u']
tmp = []
visited = [False]*C
comb(C, L)