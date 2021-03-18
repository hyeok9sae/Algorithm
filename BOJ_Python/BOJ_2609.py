# 최대공약수와 최소공배수
def gcd(num1, num2):
    while True:
        tmp = num1 % num2
        num1 = num2
        num2 = tmp
        if tmp == 0:
            break
    return num1

def lcm(num1, num2, g):
    return g * num1 // g * num2 // g

A, B = map(int, input().split())
print(gcd(A, B))
print(lcm(A, B, gcd(A, B)))