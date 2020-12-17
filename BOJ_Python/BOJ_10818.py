# 최소, 최대
N = int(input())
num = list(map(int, input().split(' ')))
# max, min = num[0], num[0]
# for i in num:
#     if max <= i:
#         max = i
#     if min >= i:
#         min = i
print("{} {}".format(min(num), max(num)))