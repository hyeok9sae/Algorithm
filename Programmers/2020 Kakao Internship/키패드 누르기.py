# 키패드 누르기
def solution(numbers, hand):
    answer = ''
    dic = {}
    num = 1
    for i in range(3):
        for j in range(3):
            dic[num] = (i, j)
            num += 1
    dic[0] = (3,1)
    ly, lx = 3, 0
    ry, rx = 3, 2
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += "L"
            ly = dic[i][0]
            lx = dic[i][1]
        elif i == 3 or i == 6 or i == 9:
            answer += "R"
            ry = dic[i][0]
            rx = dic[i][1]
        else:
            dist_left = abs(dic[i][0] - ly)+abs(dic[i][1] - lx)
            dist_right = abs(dic[i][0] - ry)+abs(dic[i][1] - rx)
            if dist_left != dist_right:
                if dist_left > dist_right:
                    answer += "R"
                    ry = dic[i][0]
                    rx = dic[i][1]
                else:
                    answer += "L"
                    ly = dic[i][0]
                    lx = dic[i][1]
            else:
                if hand == "right":
                    answer += "R"
                    ry = dic[i][0]
                    rx = dic[i][1]
                else:
                    answer += "L"
                    ly = dic[i][0]
                    lx = dic[i][1]
    # print(answer)
    return answer

# solution([1,3,4,5,8,2,1,4,5,9,5], "right")