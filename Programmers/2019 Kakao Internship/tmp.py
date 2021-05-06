def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')
    print(s1)
    new_s = []
    for i in s1:
        new_s.append(i.split(','))
    print(new_s)
    new_s.sort(key = len)
    print(new_s)
    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer

solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")