# 약수
while True:
    try:
        n = int(input())
    except:
        break
    num = 1
    while True:
        if num % n == 0:
            print(len(str(num)))
            break
        num = num*10 + 1