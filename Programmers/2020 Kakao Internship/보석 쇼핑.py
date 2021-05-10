# 보석 쇼핑
def solution(gems):
    answer = []
    dic = {}
    for i in range(gems):
        if lst[i] not in dic:
            dic[lst[i]] = i

    return answer

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])