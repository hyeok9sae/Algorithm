# 나이순 정렬
N = int(input())
lst = list()
for i in range(N):
    age, name = map(str, input().split())
    lst.append((int(age), name, i))
    
lst = sorted(lst, key=lambda index: index[2])
lst = sorted(lst, key=lambda age: age[0])

for i, j, k in lst:
    print(i, j)
