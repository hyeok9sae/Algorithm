# 수식 최대화
from itertools import permutations as pm
from collections import deque
import copy

def solution(expression):
    answer = 0
    deq = deque([])
    que = deque([])
    tmp = ""
    for i in expression:
        if '0' <= i <= '9':
            tmp += i
            continue
        que.append(int(tmp))
        que.append(i)
        tmp = ""
    que.append(int(tmp))
    # print(deq)

    operation = ['*','+','-']
    for i in pm(operation):
        # max = 
        deq = copy.deepcopy(que)
        # print(deq)
        for j in range(len(operation)):
            op = i[j]
            # print(op)
            deq2 = deque([])
            while deq:
                if len(deq) == 1:
                    deq2.append(deq.popleft())
                    break
                a = deq.popleft()
                oper = deq.popleft()
                if oper != op:
                    deq2.append(a)
                    deq2.append(oper)
                    continue
                else:
                    b = deq.popleft()
                    if oper == '+':
                        deq.appendleft(a+b)
                    elif oper == '-':
                        deq.appendleft(a-b)
                    else:
                        deq.appendleft(a*b)
            deq = deq2
        if answer < abs(deq[0]):
            answer = abs(deq[0])
    # print(answer)
    return answer

# solution("50*6-3*2")