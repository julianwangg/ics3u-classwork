message = input("What is your message? ")

print()
print(f"Your message is {len(message)} characters long.")
print(f"The first character is at position 0 and is '{message[0]}'.")
lastpos = len(message) - 1
print(f"The last character is at position {lastpos} and is '{message[lastpos]}'.")
print()
print("Here are all the characters, one at a time:\n")

for i in range(len(message)):
    print(f"\t{i} - '{message[i]}'")

vowels = 'aeiouAEIOU'
vowel_count = 0
for i in range(len(message)):
    if message[i] in vowels:
        vowel_count += 1

print(f"\nYour message contains {vowel_count} vowels.")


#The output is range 0 to 7 (0,7)
#For a list, it prints out each integer before 7 (0 1 2 3 4 5 6)
#For 'Hello', the length is 5 so the range include 0 1 2 3 4
#The length of the message is 3 and the index is 2
