from collections import deque

def solution(priorities, location):
    answer = 0
    count = 0
    deq = deque()
    for i in range(len(priorities)):
        deq.append((priorities[i], i))
    while deq:
        if deq[0][0] < max(priorities):
            deq.append(deq.popleft())
            priorities.append(priorities.pop(0))
        else:
            ans = deq.popleft()
            priorities.pop(0)
            count += 1
            if ans[1] == location:
                answer = count

    # print(answer)
    return answer

# priorities = [1,1,9,1,1,1]
# location = 0
# solution(priorities, location)