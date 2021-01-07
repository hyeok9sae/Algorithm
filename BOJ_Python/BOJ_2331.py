# 반복수열
A, P = map(int, input().split())
dic = {}
A = str(A)
dic[A] = 0
idx = 1
while True:
    tmp = 0
    for i in A:
        tmp += int(i)**P
    A = str(tmp)
    if A in dic:
        print(dic[A])
        break
    else:
        dic[A] = idx
        idx += 1

'''
def dfs(A, count):
    if check[A] != 0:
        return check[A]-1
    check[A] = count
    count += 1
    num = 0
    for i in str(A):
        num += int(i)**P
    return dfs(num, count)

# 바깥의 변수를 함수에서 조작시 파라미터로 넘겨주거나 global선언
# 참조는 그냥 가능
A, P = map(int, input().split())
check = [0]*250000
count = 1
print(dfs(A, count))
'''