def solution(array, commands):
    answer = []
    tmp = []
    for i, j, k in commands:
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])

    # print(answer)
    return answer

# array = [1,5,2,6,3,7,4]
# commands = [[2,5,3],[4,4,1],[1,7,3]]
# solution(array, commands)