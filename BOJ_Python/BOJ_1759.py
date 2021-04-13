# 암호 만들기
def comb(start, n, r):
    if r == 0:
        if check(tmp):
            print(*tmp, sep="")
        return
    for i in range(start, n):
        tmp.append(lst[i])
        comb(i+1, n, r-1) 
        tmp.pop()   

def check(arr):
    cnt1, cnt2 = 0, 0
    for i in arr:
        if i in vowel:
            cnt1 += 1
        else:
            cnt2 += 1
    if cnt1 >= 1 and cnt2 >= 2:
        return True
    else:
        return False

L, C = map(int, input().split())
lst = list(input().split())
lst.sort()
tmp = []
vowel = ['a', 'e', 'i', 'o', 'u']
comb(0, C, L)