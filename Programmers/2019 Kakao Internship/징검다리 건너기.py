# 징검다리 건너기
def solution(stones, k):
    answer = 0
    chk = 0
    flag = False
    while not flag:
        chk = 0
        for i in range(len(stones)):
            if stones[i] == 0:
                chk += 1
                if chk == k:
                    flag = True
                    break
                continue
            stones[i] -= 1
            chk = 0
        if not flag: 
            answer += 1
    print(answer)
    return answer

solution([2,4,5,3,2,1,4,2,5,0], 10)