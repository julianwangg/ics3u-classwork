print("Type in a message, and I'll display it five times.")

message = input("Message: ")
print()

number = int(input("How many times should we print it? "))

n = 0
while n < number:
    print(f"{n * 10}. {message}")
    n += 1
# n += 1 increases the n count so that the while statement does not loop infinitely and the number goes up by 1
