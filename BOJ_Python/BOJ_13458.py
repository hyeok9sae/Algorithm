# 시험 감독
N = int(input())
A = [0] + list(map(int, input().split()))
B, C = map(int, input().split())
answer = 0
for i in A:
    if i == 0:
        continue
    if i <= B:
        continue
    if i > B:
        res = (i-B)//C
        if (i-B)%C > 0:
            answer += res+1
        else:
            answer += res
answer += len(A)-1
print(answer)