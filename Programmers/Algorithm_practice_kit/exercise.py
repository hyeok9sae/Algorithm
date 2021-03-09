def solution(x):
    answer = True
    lst = list()
    tmp = str(x)
    lst = list(map(int, tmp))
    if x % sum(lst) != 0:
        answer = False
    return answer