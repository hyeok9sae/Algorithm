# 집합
M = int(input())
s = 0
for _ in range(M):
    tmp = input().split()
    if len(tmp) == 1:
        cmd = tmp[0]
    else:
        cmd, x = tmp[0], int(tmp[1])
    if cmd == "add":
        s |= (1 << x)
    elif cmd == "remove":
        s &= ~(1 << x)
    elif cmd == "check":
        if s & (1 << x) > 0:
            print(1)
        else:
            print(0)
    elif cmd == "toggle":
        s ^= (1 << x)
    elif cmd == "all":
        s = (1 << 21) -1
    elif cmd == "empty":
        s = 0
    print(bin(s))