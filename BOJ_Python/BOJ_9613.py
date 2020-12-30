# GCD 합
def gcd(a, b):
    while True:
        if b == 0:
            return a
        tmp = a
        a = b
        b = tmp%b

t = int(input())
for _ in range(t):
    ans = 0
    lst = list(map(int, input().split()))
    for i in range(1, len(lst)):
        for j in range(2, len(lst)):
            if i >= j:
                continue
            ans += gcd(lst[i], lst[j])
    print(ans)