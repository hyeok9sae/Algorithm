# 종이의 개수
def check(row, col, num):
    tmp = matrix[row][col]
    for i in range(num):
        for j in range(num):
            if tmp != matrix[row + i][col + j]:
                devide(row, col, num//3)
                return
    result[tmp+1] += 1

def devide(row, col, num):
    for i in range(3):
        for j in range(3):
            check(row + i*num, col + j*num, num)

N = int(input())
matrix = []
result = [0, 0, 0]
for _ in range(N):
    matrix.append(list(map(int, input().split())))

check(0, 0, N)
print(*result, sep="\n")