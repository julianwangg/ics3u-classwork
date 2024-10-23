firstmsg = input("Please input your first message: ")
secondmsg = input("Please input your second message: ")
result = ""
i = 0

while i < len(firstmsg) and i < len(secondmsg):
    result += firstmsg[i] + secondmsg[i]
    i += 1

if i < len(firstmsg):
    result += firstmsg[i:]
elif i < len(secondmsg):
    result += secondmsg[i:]

print("The combined string is:", result)