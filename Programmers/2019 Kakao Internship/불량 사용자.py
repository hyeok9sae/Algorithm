# 불량 사용자
from itertools import permutations as pm

def isMatch(candidated_id, banned_id):
    for i in range(len(banned_id)):
        if len(candidated_id[i]) != len(banned_id[i]):
            return False
        for j in range(len(candidated_id[i])):
            if banned_id[i][j] == '*':
                continue
            if candidated_id[i][j] != banned_id[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    answer = 0
    ans_lst = []
    for candidated_id in pm(user_id, len(banned_id)):
        if isMatch(candidated_id, banned_id):
            candidated_id = set(candidated_id)
            if candidated_id not in ans_lst:
                ans_lst.append(candidated_id)
    # print(ans_lst)
    answer = len(ans_lst)
    return answer

# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])