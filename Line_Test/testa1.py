def solution(program, flag_rules, commands):
    answer = [True]*len(commands)
    for idx, i in enumerate(commands):
        tmp = list(map(str, i.split()))
        if tmp[0] != program:
            answer[idx] = False
            # print(tmp[0])
        for j in range(1, len(tmp), 2):
            if tmp[j] == '-n':
                chk = tmp[j+1]
                for i in chk:
                    if not '0' <= i <= '9':
                        answer[idx] = False
            elif tmp[j] == '-s':
                chk = tmp[j+1]
                for i in chk:
                    if not ('a' <= i <= 'z' or 'A' <= i <= 'Z'):
                        answer[idx] = False
            elif tmp[j] == '-e':
                    continue
            else:
                answer[idx] = False
    print(answer)
    return answer

program = "line"
flag_rules = ["-s STRING", "-n NUMBER", "-e NULL"]
commands = ["line -s 123 -n HI", "line fun"]
solution(program, flag_rules, commands)