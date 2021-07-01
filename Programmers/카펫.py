# 카펫
def solution(brown, yellow):
    answer = []
    new_brown = brown // 2 + 2
    for i in range(1, new_brown):
        row = i
        col = new_brown - i
        if row > col:
            break
        if row * col == brown + yellow:
            answer.append(col)
            answer.append(row)
            break
    # print(answer)
    return answer

solution(24, 24)