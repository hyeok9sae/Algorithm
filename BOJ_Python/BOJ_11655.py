# ROT13
msg = input()
for i in msg:
    if "A" <= i <= "Z":
        print(chr((((ord(i))-65)+13)%26+65), end='')
    elif "a" <= i <= "z":
        print(chr((((ord(i))-97)+13)%26+97), end='')
    else:
        print(i, end='')