def solution(phone_book):
    answer = True
    dic = {}
    for i in phone_book:
        dic[i] = 1
    for i in phone_book:
        tmp = ''
        for j in i:
            tmp += j
            if tmp in dic and tmp != i:
                answer = False
    print(answer)
    return answer

phone_book = ["119", "97644223", "1195524421"]
solution(phone_book)