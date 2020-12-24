# 알파벳 개수
'''
lst, alp = list(0 for _ in range(26)), list()
S = input().strip()
for i in S:
    lst[ord(i)-97] += 1

for i in lst:
    print(i, end=' ')
'''
S = input().strip()

for i in range(ord("a"), ord("z")):
    print(str(S.count(chr(i)))+" ")

