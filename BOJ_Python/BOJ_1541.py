# 잃어버린 괄호
expression = input().split("-")
ans = 0
for idx, i in enumerate(expression):
    lst = i.split("+")
    if idx == 0:
        for number in lst:
            ans += int(number)
    else:
        for number in lst:
            ans -= int(number)
print(ans)

# 처음 마이너스 연산자 이후 부터는 숫자를 전부 빼줘야 최소값이 됨