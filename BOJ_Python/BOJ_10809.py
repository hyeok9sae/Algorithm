# 알파벳 찾기
'''
alp = list(-1 for _ in range(26))
S = input().strip()
# print(S[0])
for i in range(len(S)):
    if alp[ord(S[i])-97] != -1:
        continue
    alp[ord(S[i])-97] = i

for i in alp:
    print(i, end=" ")
'''
S = input().strip()

for i in range(ord("a"), ord("z")+1):
    print(S.find(chr(i)), end=' ')