# 최소공배수
def gcd(A, B):
    while True:
        if B == 0:
            return A
        tmp = A
        A = B
        B = tmp%B

def lcm(A, B, C):
    return A*B//C

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B, gcd(A, B)))