import random
answer = random.randrange(1,11)
guesses = 0
print("I am thinking of a number from 1-10")
guess = int(input("Your guess: "))

while guess != answer:
    print("Wrong, try again")
    guess = int(input("Your guess: "))
    guesses += 1
print(f"howd u know, u took {guesses} guesses")