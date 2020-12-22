# 괄호
N = int(input())
lst = list()
for _ in range(N):
    lst = input()
    stack = list()
    for i in lst:
        if i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
                continue
            stack.append(i)
        stack.append(i)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
