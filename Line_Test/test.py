def solution(table, languages, preference):
    answer = ''
    matrix = {}
    res = []
    for i in table:
        tmp = i.split()
        # print(tmp)
        matrix[tmp[0]] = {tmp[t]:len(tmp)-t for t in range(1, len(tmp))}
    # print(matrix)
    # res = float('-inf')
    for i in matrix:
        # print(matrix[i])
        ans = 0
        for j in range(len(languages)):
            if languages[j] in matrix[i]:
                ans += preference[j] * matrix[i][languages[j]]
        res.append((ans, i))
    res.sort(key= lambda x: x[1])
    res.sort(key= lambda x: x[0], reverse=True)
    answer = res[0][1]
    print(answer)


    return answer

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
solution(table, languages, preference)