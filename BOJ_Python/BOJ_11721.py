# 열 개씩 끊어 출력하기
msg = input()
for i in range(0, len(msg), 10):
    print(msg[i:i+10])

