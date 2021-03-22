def solution(N, stages):
    answer = []
    lst = [0]*(N+2)
    dic = {}
    for i in stages:
        lst[i] += 1
    comple = len(stages)
    for i in range(1, N+1):
        if comple == 0:
            dic[i] = 0
            continue
        dic[i] = lst[i] / comple
        comple -= lst[i]
    # print(dic)
    answer = sorted(dic, key= lambda x : dic[x], reverse=True)
    # print(answer)
    return answer

# N = 4
# stages = [1,1,1,1,1]
# solution(N, stages)