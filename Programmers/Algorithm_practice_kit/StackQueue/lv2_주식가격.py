from collections import deque

def solution(prices):
    answer = []
    deq = deque(prices)
    while deq:
        count = 0
        tmp = deq.popleft()
        for i in deq:
            if i >= tmp:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
    # print(answer)
    return answer

# prices = [1, 2, 3, 2, 3]
# solution(prices)/