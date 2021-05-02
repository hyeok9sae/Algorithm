# 탑
N = int(input())
lst = list(map(int, input().split()))
stack = []
dic = {}
ans = []
for idx, val in enumerate(lst):
    dic[val] = idx
    while True:
        if len(stack) == 0:
            stack.append(val)
            ans.append(0)
            break
        if stack[-1] > val:
            ans.append(dic[stack[-1]]+1)
            stack.append(val)
            break
        else:
            stack.pop()
print(*ans)