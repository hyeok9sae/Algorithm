# 2007년
x, y = map(int, input().split())
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month_30 = [4, 6, 9, 11]
ans = 0
for i in range(1, x):
    # print(i)
    if i == 2:
       ans += 28
    elif i in month_30:
        ans += 30
    else:
        ans += 31
ans += y
# print(ans)
print(week[ans%7])
