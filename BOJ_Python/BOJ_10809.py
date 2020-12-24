# 알파벳 찾기
alp = list(-1 for _ in range(26))
S = input().split()
print(S[0])
for i in range(len(S)):
    # if alp[ord(S[i])-65] != -1:
    #     continue
    alp[ord(S[i])-65] = i

for i in alp:
    print(i, end=" ")