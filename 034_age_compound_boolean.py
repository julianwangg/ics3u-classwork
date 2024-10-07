name = input("What is your name? ")
age = int(input("What is your age? "))

if age < 16 and age >= 0:
    print(f"you can't drive {name}.")
elif age >= 16 and age <= 17:
    print(f"you can drive but not vote {name}")
elif age >= 18 and age <=24:
    print(f"You can vote but can't rent a car, {name}")
elif age >= 25:
    print(f"You can do pretty much anything {name}!")
