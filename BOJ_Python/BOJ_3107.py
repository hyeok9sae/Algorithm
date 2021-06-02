# IPv6
ip = input().split(":")
ans = ""
flag = False
for i in ip:
    size = 4 - len(i)
    if flag and size == 4:
        continue
    if not flag and size == 4:
        cnt = 0
        for j in ip:
            if j == '':
                continue
            cnt += 1
        for _ in range(8-cnt):
            ans += '0000:'
        flag = True
        continue
    ans += '0'*size + i +':'
print(ans[:-1])