def solution(inp_str):
    answer = []
    #1
    if 8 <= len(inp_str) <= 15:
        pass
    else:
        answer.append(1)
    #2
    spe = ['~','!','@','#','$','%','^','&','*']
    for i in inp_str:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z' or '0' <= i <= '9' or i in spe:
            pass
        else:
            answer.append(2)
            break
    #3
    check = [0]*4
    for i in inp_str:
        if 'a' <= i <= 'z':
            check[0] = 1
        elif 'A' <= i <= 'Z':
            check[1] = 1
        elif '0' <= i <= '9':
            check[2] = 1
        elif i in spe:
            check[3] = 1
    count = 0
    for i in check:
        if i == 0:
            count += 1
    if count > 1:
        answer.append(3)
    #4
    chk = 0
    k = inp_str[0]
    for i in inp_str:
        if chk == 4:
            answer.append(4)
            break
        if k == i:
            k = i
            chk += 1

    #5
    dic = {}
    for i in inp_str:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic:
        if dic[i] >= 5:
            answer.append(5)

    if len(answer) == 0:
        answer.append(0)
    print(answer)
    return answer

inp_str = "ZzZz9Z824"	
solution(inp_str)