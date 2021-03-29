def solution(new_id):
    # 1단계
    answer = new_id.lower()
    # 2단계
    tmp = ''
    for i in answer:
        if 'a' <= i <= 'z' or i == '-' or i == '_' or i == '.' or '0' <= i <= '9':
            tmp += i
    answer = tmp
    # 3단계
    tmp_a, tmp_b = '', ''
    for i in answer:
        if tmp_a == '.' and i == '.':
            continue
        tmp_a = i
        tmp_b += tmp_a
    answer = tmp_b
    # 4단계
    if len(answer) > 0:
        if answer[0] == '.':
            answer = answer[1:]
    if len(answer) > 0:
        if answer[-1] == '.':
            answer = answer[:len(answer)-1]
    # 5단계
    if answer == '':
        answer += 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:len(answer)-1]
    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    print(answer)
    return answer

# solution("12345678901234.67")