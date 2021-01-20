# 숫자 카드 2
# def binary_search(start, end, num):
#     while start <= end:
#         mid = (start + end) // 2
#         if num > num_lst2[mid]:
#             start = mid + 1
#         elif num == num_lst2[mid]:
#             return dic[num]
#         else:
#             end = mid - 1
#     return 0

N = int(input())
num_lst = list(map(int, input().split()))
# print(num_lst, num_lst2)
dic = {}
# for i in num_lst:
#     dic[i] = num_lst.count(i)
# print(dic)
M = int(input())
find_lst = list(map(int, input().split()))
for i in num_lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for i in find_lst:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")