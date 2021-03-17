# 약수의 합 2
N = int(input())
num = 1
ans = 0
while num <= N:
    ans += (N // num) * num 
    num += 1
print(ans)