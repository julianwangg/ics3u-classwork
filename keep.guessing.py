import random
answer = random.randrange(1,11)

print("I am thinking of a number from 1-10")
guess = int(input("Your guess: "))

while guess != answer:
    print("Wrong, try again")
    guess = int(input("Your guess: "))
print("howd u know")