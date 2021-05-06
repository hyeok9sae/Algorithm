# 크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    lst = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            toy = board[j][i-1]
            board[j][i-1] = 0
            if len(lst) != 0:
                if lst[-1] == toy:
                    lst.pop()
                    answer += 2
                else:
                    lst.append(toy)
            else:
                lst.append(toy)
            break
    # print(answer)
    return answer

# solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])