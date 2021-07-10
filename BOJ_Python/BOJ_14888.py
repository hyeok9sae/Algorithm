# 연산자 끼워넣기
def operation(operator):
    if operator == '+':

    elif operator == '-':
    elif operator == '*':
    else:


def dfs(num, r):
    if r >= len(oper_lst):
        return
    for i in range(len(oper_lst)):
        if not visited[i]:
            visited[i] = True
            dfs(oper_lst[i], r+1)
            visited[i] = False

N = int(input())
lst = list(map(int, input().split()))
oper = list(map(int, input().split()))
oper_lst = []
for idx, i in enumerate(oper):
    for j in range(i):
        if idx == 0:
            oper_lst.append('+')
        elif idx == 1:
            oper_lst.append('-')
        elif idx == 2:
            oper_lst.append('*')
        else:
            oper_lst.append('/')
visited = [False]*(len(oper_lst))
dfs(lst[0], 0)
# print(-7//3+1)