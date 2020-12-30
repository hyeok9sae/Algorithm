# 최대공약수
def gcd(A, B):
    while True:
        if B == 0:
            return A
        tmp = A
        A = B
        B = tmp%B

A, B = map(int, input().split())
print(str("1")*gcd(A,B))
