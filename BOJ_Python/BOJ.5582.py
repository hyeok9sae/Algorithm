# 공통 부분 문자열
stringA, stringB = '0'+input(), '0'+input()
matrix = [[0]*len(stringB) for _ in range(len(stringA))]
answer = 0
for i in range(1, len(stringA)):
    for j in range(1, len(stringB)):
        if stringA[i] == stringB[j]:
            matrix[i][j] = matrix[i-1][j-1] + 1
            answer = max(answer, matrix[i][j])
print(answer)