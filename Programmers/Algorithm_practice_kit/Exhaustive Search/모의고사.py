def solution(answers):
    answer = []
    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == person1[i%len(person1)]:
            cnt1 += 1
        if answers[i] == person2[i%len(person2)]:
            cnt2 += 1
        if answers[i] == person3[i%len(person3)]:
            cnt3 += 1
    tmp = [cnt1, cnt2, cnt3]
    for i in range(len(tmp)):
        if max(tmp) == tmp[i]:
            answer.append(i+1)
    answer.sort()
    print(answer)

    return answer

answers = [1,3,2,4,2]
solution(answers)