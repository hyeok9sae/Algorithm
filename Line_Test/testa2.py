def solution(program, flag_rules, commands):
    # commands의 크기에 맞게 answer배열을 True 값으로 초기화
    answer = [True]*len(commands)
    # commands의 원소별로 명령어 규약을 지키는지 판별하기 위한 반복문
    for idx, i in enumerate(commands):
        # 명령어 규약을 판별하기 위한 임시 배열 생성
        tmp = list(map(str, i.split()))
        if tmp[0] != program:
            answer[idx] = False
            # print(tmp[0])
        if tmp[0] == "line":
            j = 1
            while j <= len(tmp)-1:
                # flag argument type 의 flag argumet값인지 조건문으로 검사
                if tmp[j] == '-n': #-n
                    j += 1
                    while j <= len(tmp)-1:
                        if tmp[j][0] == '-':
                            # print(tmp[j][0])
                            # j += 1
                            break
                        chk = tmp[j]
                        for c in chk:
                            if not '0' <= c <= '9':
                                answer[idx] = False
                        j += 1

                elif tmp[j] == '-s': #-s
                    j += 1
                    while j <= len(tmp)-1:
                        if tmp[j][0] == '-':
                            # print(tmp[j][0])
                            # j += 1
                            break
                        chk = tmp[j]
                        for c in chk:
                            if not ('a' <= c <= 'z' or 'A' <= c <= 'Z'):
                                answer[idx] = False
                        j += 1

                elif tmp[j] == '-e': #-e
                    j += 1
                    continue
                
                # -e 다음 null값이 오지 않고 argument 값이 등장한다면
                # 규약을 어기는 것이므로 다음 조건검사에서 type 검사 세가지
                # 조건에 부합하지 않으므로 바로 else문으로 빠져서 False 리턴
                else:
                    answer[idx] = False
                    j += 1
        if tmp[0] == "trip":
            j = 1
            while j <= len(tmp)-1:
                # flag argument type 의 flag argumet값인지 조건문으로 검사
                if tmp[j] == '-days': #-n
                    j += 1
                    while j <= len(tmp)-1:
                        if tmp[j][0] == '-':
                            # print(tmp[j][0])
                            # j += 1
                            break
                        chk = tmp[j]
                        for c in chk:
                            if not '0' <= c <= '9':
                                answer[idx] = False
                        j += 1

                elif tmp[j] == '-dest': #-s
                    j += 1
                    k = 0
                    while j <= len(tmp)-1:
                        if tmp[j][0] == '-':
                            # print(tmp[j][0])
                            # j += 1
                            break
                        if k != 0 and flag_rules[idx][1][-1] != 'S':
                            answer[idx] = False
                            break
                        # if flag_rules[idx][1][-1] != 'S':
                        #     answer[idx] = False
                        #     break
                        chk = tmp[j]
                        for c in chk:
                            if not ('a' <= c <= 'z' or 'A' <= c <= 'Z'):
                                answer[idx] = False
                        k = 1
                        j += 1
                # -e 다음 null값이 오지 않고 argument 값이 등장한다면
                # 규약을 어기는 것이므로 다음 조건검사에서 type 검사 세가지
                # 조건에 부합하지 않으므로 바로 else문으로 빠져서 False 리턴
                else:
                    answer[idx] = False
                    j += 1
    print(answer)
    return answer

program = "trip"
flag_rules = ["-days NUMBERS", "-dest STRING"]
commands = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]
solution(program, flag_rules, commands)