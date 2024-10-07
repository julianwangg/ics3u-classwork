import random
answer = random.randrange(1,11)

print("I am thinking of a number from 1-10")
guess = int(input("Your guess: "))

if guess == answer:
    print("Dang how did you know that!?")
elif guess <=0 or guess >=10:
    print("Please enter number from 1-10")
else: print(f"The answer is {answer}")