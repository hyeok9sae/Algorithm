# 괄호 추가하기
from collections import deque

def solve(count, flag, tmp):
    if count == N//2:
        lst.append(tmp)
        return
    if flag:
        solve(count+1, False, tmp+[0])
    else:
        solve(count+1, True, tmp+[1])
        solve(count+1, False, tmp+[0])

def cal(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    else:
        return num1 * num2
    
N = int(input())
equa = input()
lst, max_answer = [], []
solve(0, False, [])
for tc in lst:
    i, deq = 0, deque()
    # print(tc)
    while i < N:
        if i % 2 == 0:
            deq.append(int(equa[i]))
        else:
            if tc[i//2] == 1:
                oper = equa[i]
                deq.append(cal(deq.pop(), int(equa[i+1]), oper))
                i += 1
            else:
                deq.append(equa[i])
        i += 1
    answer = deq.popleft()
    while deq:
        oper = deq.popleft()
        answer = cal(answer, deq.popleft(), oper)
    max_answer.append(answer)
print(max(max_answer))