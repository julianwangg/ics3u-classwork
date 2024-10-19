x = 0
while x <= 10:
    if x == 7:
        x+=1
        continue
    print(x)
    x+=1

total = 0
for number in range(5, 21):
    if number % 3 != 0:
        total += number

print(f"The total is {total}")

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

total = 0

for number in range(start, end + 1):
    if number == 13 or number == 31:
        break
    total += number

print(f"the sum of numbers from {start} to {end}, stopping if 13 or 31 comes across, is: {total}")

while True:
    word = input("enter word: ")
    if word == "stop":
        break
    print(f"your word: {word}")
    
print("cya!")