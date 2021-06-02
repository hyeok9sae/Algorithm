# 부분 문자열
def check(idx):
    for i in range(1, len(P)):
        if idx >= len(S):
            return False
        if P[i] != S[idx]:
            return False
        idx += 1
    return True

S, P = input(), input()
flag = False
for i in range(len(S)):
    if S[i] == P[0]:
        if check(i+1):
            print(1)
            flag = True
            break
        i += len(P)
if not flag:
    print(0)