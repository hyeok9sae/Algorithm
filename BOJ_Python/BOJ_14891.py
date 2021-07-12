# 톱니바퀴
def rotate(num, dir):
    visited[num] = True
    if dir == -1:
        if num+1 < 4 and not visited[num+1] and lst[num][2] != lst[num+1][6]:
            rotate(num+1, 1)
        if num-1 >= 0 and not visited[num-1] and lst[num][6] != lst[num-1][2]:
            rotate(num-1, 1)
        lst[num].append(lst[num].pop(0))
    else:
        if num+1 < 4 and not visited[num+1] and lst[num][2] != lst[num+1][6]:
            rotate(num+1, -1)
        if num-1 >= 0 and not visited[num-1] and lst[num][6] != lst[num-1][2]:
            rotate(num-1, -1)
        lst[num].insert(0, lst[num].pop())
    
lst = []
for _ in range(4):
    lst.append(list(input()))
K = int(input())
for _ in range(K):
    num, dir = map(int, input().split())
    visited = [False]*4
    rotate(num-1, dir)
answer = 0
for i in range(4):
    answer += int(lst[i][0])*(2**i)
print(answer)