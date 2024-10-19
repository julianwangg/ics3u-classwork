import random
print("I am thinking of a number from 1-100")
guesses = 0
ans = random.randint(1,100)
user_ans = int(input("Take your best guess: "))
while user_ans != ans and guesses <= 7:
    if user_ans > ans:
        print("Too high")
    elif user_ans < ans:
        print("Too low")
    elif user_ans == ans:
        print("how did u get that??")
    guesses +=1 
    user_ans = int(input("Take your best guess: "))

print(f"the answer was {ans}!")
