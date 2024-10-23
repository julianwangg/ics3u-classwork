msg = input("What is your input?")
i = 0
found = False
while i < len(msg) -2:
    if msg[i] == "b" and msg[i+2]== "b":
        found = True
        break
    i +=1
if found:
    print(True)
else:
    print(False)