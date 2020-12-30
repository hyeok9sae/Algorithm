# 최대공약수와 최소공배수
def gcd(a, b):
    while True:
        if b == 0:
            return a
        tmp = a
        a = b
        b = tmp%b
def lcm(a, b, c):
    return a*b//c
a, b = map(int, input().split())
c = gcd(a, b)
print(c)
print(lcm(a, b, c))