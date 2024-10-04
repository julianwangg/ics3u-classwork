name = input("Whats your name? ")
age = int(input(f"hello {name}, how old are you? "))
if age <16:
    print("you can't drive yet dude!")
elif 16<= age <= 17: 
    print(f"congrats {name}! you can drive now but you cant vote just yet!")
elif age == 18: 
    print(f"congrats {name}! you can vote now!")
elif age == 19:
    print(f"congrats {name}! you can drink, and drive, but not at the same time of course!")
elif age == 20: 
    print(f"hey {name}, you are one year away from being able to do anything legal in the US!")
elif age == 21: 
    print(f"congrats {name}! you are legal age in the US now!")
else: print(f"congrats {name} you can do anything you want that is legal!")