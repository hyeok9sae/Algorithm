def solution(participant, completion):
    
    dic = {}
    for i in completion:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    # print(dic)
    for i in participant:
        if i in dic and dic[i] != 0:
            dic[i] -= 1
        else:
            answer = i
    # print(dic)
    # print(answer)
    return answer

# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]
# solution(participant, completion)