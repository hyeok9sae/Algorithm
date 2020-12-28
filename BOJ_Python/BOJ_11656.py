# 접미사 배열
S = input()
lst = list()
for i in range(len(S)):
    tmp = S[i:]
    lst.append(tmp)  
lst = sorted(lst) 
for i in lst:
    print(i)