import math

while True:
    num = int(input("Give me a number you want to be square rooted!: "))
    if num >= 0:
        print(f"The square root of your number is: {math.sqrt(num)}")
        break
    else:
        print("Only a positive number can be square rooted silly")
        continue
