msg = input("What is your message: ")
n = int(input("What is your number? "))
result = ""
last_chars = msg[-n:]

for i in range(n):
    result += last_chars

print(result)