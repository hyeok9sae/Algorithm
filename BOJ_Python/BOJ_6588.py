# 골드바흐의 추측
def is_prime(num):
    if num < 2:
        return
    i = num
    while num*i <= MAX:
        if array[num*i] == 0:
            array[num*i] = 1
        i += 1

MAX = 1000000
array = [0]*(MAX+1)
for i in range(2, MAX+1):
        if array[i] == 0:
            is_prime(i)
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(2, n-1):
        if array[i] == 0 and array[n-i] == 0:
            print(f"{n} = {i} + {n-i}")
            break