from collections import Counter

def init(str):
    if 'a' <= str[0] <= 'z' or 'A' <= str[0] <= 'Z':    
        if 'a' <= str[1] <= 'z' or 'A' <= str[1] <= 'Z':
            return True
    return False

def solution(str1, str2):
    answer = 0
    lst1, lst2 = [], []
    tmp = ""
    for i in range(len(str1)-1):
        if init(str1[i:i+2]):
            tmp += str1[i:i+2]
            lst1.append(tmp.upper())
        tmp = ""
    for i in range(len(str2)-1):
        if init(str2[i:i+2]):
            tmp += str2[i:i+2]
            lst2.append(tmp.upper())
        tmp = ""
    if len(lst2) == 0:
        return 65536
    count_lst1 = Counter(lst1)
    count_lst2 = Counter(lst2)
    count_lst3 = count_lst1 & count_lst2
    count_lst4 = count_lst1 | count_lst2
    res = sum(count_lst3.values()) / sum(count_lst4.values())
    answer = int(res * 65536)
    # print(answer)
    return answer

# str1 = "E=M*C^2"
# str2 = "e=m*c^2"
# solution(str1, str2)