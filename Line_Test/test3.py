def solution(enter, leave):
    answer = [0]*3
    for i in enter:
        for j in leave:
            if i == j:
                answer[i-1] += 1
    print(answer)
    return answer

enter = [1,3,2]
leave = [1,2,3]
solution(enter, leave)