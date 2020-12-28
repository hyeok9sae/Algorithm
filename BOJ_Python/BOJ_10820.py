# 문자열 분석
while True:
    try:
        msg = input() # strip()는 입력 문자열의 공백이 제거
        a, b, c, d = 0, 0, 0, 0
        for i in msg:
            if "a" <= i <= "z":
                a += 1
            if "A" <= i <= "Z":
                b += 1
            if  "0" <= i <= "9":
                c += 1
            if i == " ":
                d += 1
        print(a, b, c, d)
    except:
        break