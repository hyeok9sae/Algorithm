# 튜플
from collections import deque

def solution(s):
    answer = []
    lst = []
    tmp = []
    st = ""
    for i in s[:-1]:
        if i == "{" or i == ",":
            if i == ',' and st != "":
                tmp.append(int(st))
                st = ""
            continue
        if i == "}":
            tmp.append(int(st))
            st = ""
            lst.append(tmp)
            tmp = []
            continue
        st += i

    # print(lst)
    lst = sorted(lst, key = lambda x : len(x))
    for i in lst:
        for j in i:
            if j not in answer:
                answer.append(j)
    # print(lst)
    print(answer)
    return answer

solution("{{20,111},{111}}")