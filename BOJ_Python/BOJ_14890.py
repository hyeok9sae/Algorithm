# 경사로
def check_y(num):
    std_num = matrix[num][0]
    cnt = 1
    flag = False
    for i in range(1, N):
        if std_num == matrix[num][i]:
            cnt += 1
        elif std_num < matrix[num][i]:
            if matrix[num][i]-std_num > 1:
                return False
            if cnt < L:
                return False
            cnt = 1
        else:
            if flag:
                return False
            if std_num-matrix[num][i] > 1:
                return False
            flag = True
            cnt = 1
        std_num = matrix[num][i]
        if flag:
            if cnt >= L:
                flag = False
                cnt = 0
    if flag:
        return False
    return True

def check_x(num):
    std_num = matrix[0][num]
    cnt = 1
    flag = False
    for i in range(1, N):
        if std_num == matrix[i][num]:
            cnt += 1
        elif std_num < matrix[i][num]:
            if matrix[i][num]-std_num > 1:
                return False
            if cnt < L:
                return False
            cnt = 1
        else:
            if flag:
                return False
            if std_num-matrix[i][num] > 1:
                return False
            flag = True
            cnt = 1
        if flag:
            if cnt >= L:
                flag = False
                cnt = 0
        std_num = matrix[i][num]
    if flag:
        return False
    return True

N, L = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]
ans = 0
for i in range(N):
    if check_y(i):
        ans += 1
        # print(i)
    if check_x(i):
        ans += 1
        # print(i)
print(ans)