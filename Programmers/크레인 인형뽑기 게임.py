def solution(board, moves):
    answer = 0
    size = len(board)
    stack = []
    for i in moves:
        for j in range(size):
            if board[j][i-1] != 0:
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                for i in range(2):
                    stack.pop()
                    answer += 1
    print(answer)
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])