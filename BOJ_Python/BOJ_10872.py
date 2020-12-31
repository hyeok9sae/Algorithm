# 팩토리얼 0의 개수
def fact(N):
    if N == 0:
        return 1
    return N * fact(N-1)
N = int(input())
lst = list(str(fact(N)))
cnt = 0
while True:
    if lst.pop() != "0":
        print(cnt)
        break
    cnt += 1