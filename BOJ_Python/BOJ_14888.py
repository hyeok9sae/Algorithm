# 연산자 끼워넣기
def dfs(res, r):
    if r >= N-1:
        answer.append(res)
        return
    for i in range(len(oper_lst)):
        if not visited[i]:
            visited[i] = True
            dfs(operation(res, i, r+1), r+1)
            visited[i] = False

def operation(res, v, r):
    if oper_lst[v] == '+':
        res += lst[r]
    elif oper_lst[v] == '-':
        res -= lst[r]
    elif oper_lst[v] == '*':
        res *= lst[r]
    else:
        if res < 0:
            res = ((res*-1)//lst[r])*-1
        else:
            res //= lst[r]
    return res

N = int(input())
lst = list(map(int, input().split()))
oper = list(map(int, input().split()))
oper_lst = []
answer = []
for i in range(len(oper)):
    for j in range(oper[i]):
        if i == 0:
            oper_lst.append('+')
        elif i == 1:
            oper_lst.append('-')
        elif i == 2:
            oper_lst.append('*')
        else:
            oper_lst.append('/')
visited = [False]*len(oper_lst)
res = lst[0]
dfs(res, 0)
print(f'{max(answer)}\n{min(answer)}')