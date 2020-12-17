# 그대로 출력하기
while(True):
    try:
        msg = input()
        print(msg)
    except EOFError:
        break