def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        dic[i[1]] = []
    for i, j in clothes:
        dic[j].append(i)
    for i in dic:
        answer *= len(dic[i])+1
    return answer - 1

# clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# solution(clothes)