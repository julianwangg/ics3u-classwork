str1 = input("Whats your first message:")
str2 = input("Whats your second message:")

if str1[-len(str2):] == str2:
    print("True")
else: print("False")