# 수 이어 쓰기 1
N = input()
size = len(N)
num = int(N)
ans = 0
while size >= 1:
    ans += (num-10**(size-1)+1)*size
    num = 10**(size-1)-1
    size-=1
print(ans)