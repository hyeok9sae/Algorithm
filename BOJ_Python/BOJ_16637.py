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
lst, i = [], 0
deq = deque()
solve(0, False, [])
while i < N:
    if i % 2 == 0:
        deq.append(int(equa[i]))
    else:
        if lst[i//2] == 1:
            oper = equa[i]
            deq.append(cal(deq.pop(), int(equa[i+1]), oper))
            i += 1
        else:
            deq.append(equa[i])
    i += 1
print(deq)
