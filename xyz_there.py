msg = input("please input your string: ").lower()
i = 0

while i < len(msg) - 2:
    if msg[i:i+3] == "xyz" and (i == 0 or msg[i - 1] != '.'):
        print("true")
        break
    i += 1
else:
    print("False")