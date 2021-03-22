# 소수 찾기
def prime_num(number):
    if number == 1:
        return False
    j = 2
    while j*j <= number:
        if number % j == 0:
            return False
        j += 1
    return True

N = int(input())
lst = list(map(int, input().split()))
answer = 0
for i in lst:
    if prime_num(i):
        answer += 1
print(answer)