# 부등호
def perm(r):
    if r == k+1:
        s = ""
        for i in tmp:
            s += str(i)
        ans.append(s)
        return
    for i in range(10):
        if visited[i]:
            continue
        if lst[r-1] == '<':
            if tmp[-1] < i:
                tmp.append(i)
                visited[i] = True
                perm(r+1)
                tmp.pop()
                visited[i] = False
        else:
            if tmp[-1] > i:
                tmp.append(i)
                visited[i] = True
                perm(r+1)
                tmp.pop()
                visited[i] = False

k = int(input())
lst = input().split()
arr = [i for i in range(10)]
visited = [False]*10
tmp, ans = [], []
for i in range(10):
    tmp.append(i)
    visited[i] = True
    perm(1)
    tmp.pop()
    visited[i] = False
print(ans[-1], ans[0])