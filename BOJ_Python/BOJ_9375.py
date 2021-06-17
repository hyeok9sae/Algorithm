# 패션왕 신해빈
T = int(input())
for _ in range(T):
    n = int(input())
    dic = {}
    for _ in range(n):
        a, b = map(str, input().split())
        if b not in dic:
            dic[b] = []
        dic[b].append(a)
    answer = 1
    for i in dic:
        answer *= len(dic[i])+1
    print(answer-1)