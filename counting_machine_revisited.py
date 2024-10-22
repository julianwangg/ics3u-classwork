num1 = int(input("Give me a number you want me to count to! "))
num2 = int(input("Give me a number you want me to count from! "))
num3 = int(input("Give me a number you want me to count by! "))
for i in range (num1, num2+1, num3):
    print(i)