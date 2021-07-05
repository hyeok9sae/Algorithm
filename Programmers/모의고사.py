def solution(answers):
    answer = []
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    lst = [[i, 0] for i in range(1, 4)]
    for i in range(len(answers)):
        if answers[i] == student1[i%len(student1)]:
            lst[0][1] += 1
        if answers[i] == student2[i%len(student2)]:
            lst[1][1] += 1
        if answers[i] == student3[i%len(student3)]:
            lst[2][1] += 1
    lst.sort(key=lambda x:x[1], reverse=True)
    max_value = lst[0][1]
    for i in lst:
        if i[1] != max_value or i[1] == 0:
            break 
        answer.append(i[0])
    # print(answer)
    return answer

# solution([1,2,3,4,5])