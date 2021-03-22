# 소수 구하기
def is_prime(num):

    i = num
    while num*i <= N:
        if array[num*i] == 0:
            array[num*i] = 1
        i += 1

M, N = map(int, input().split())
array = [0]*(N+1)
for i in range(2, N+1):
    if array[i] == 0:
        is_prime(i)
for i in range(M, len(array)):
    if i == 0 or i == 1:
        continue
    if array[i] == 0:
        print(i)


'''
def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

M, N = map(int, input().split())
for i in range(M, N+1):
    if is_prime(i):
        print(i)
'''