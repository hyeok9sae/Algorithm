# 국영수
N = int(input())
lst = list()
for _ in range(N):
    name, kor, eng, mat = map(str, input().split())
    lst.append((name, int(kor), int(eng), int(mat)))
lst = sorted(lst, key=lambda name: name[0])
lst = sorted(lst, key=lambda mat: mat[3], reverse=True)
lst = sorted(lst, key=lambda eng: eng[2])
lst = sorted(lst, key=lambda kor: kor[1], reverse=True)
for i, j, k, l in lst:
    print(i)