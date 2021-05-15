# 문자열 반복
T = int(input())
for _ in range(T):
    R, S = map(str, input().split())
    for i in S:
        print(int(R)*i, end="")
    print()