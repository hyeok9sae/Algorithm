# 징검다리 건너기
import copy

def solution(stones, k):
    answer = 0
    left, right = 0, 200000000
    while left <= right:
        mid = (left+right)//2
        tmp = copy.deepcopy(stones)
        # print(tmp)
        for i in range(len(tmp)):
            tmp[i] -= mid
        
        cnt = 0
        flag = False
        for i in range(len(tmp)):
            if tmp[i] <= 0:
                cnt += 1
            else:
                cnt = 0
            
            if cnt >= k:
                flag = True
                break
        
        if flag:
            right = mid-1
        else:
            left = mid+1
    answer = left
    # print(answer)
    return answer

# solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)