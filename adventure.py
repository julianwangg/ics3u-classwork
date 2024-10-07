print("Welcome to Julian's Tiny Adventure!")
print("")
print("")

adv0 = input("Welcome to Julian's Mansion! Would you like to enter for the chance to win some money?? ")
if adv0 == "yes":
    print("Wonderful! Welcome in!")
else: print("Too bad, come on in!")

adv1 = input("You are now in Julian's Mansion! Would you like to go Upstairs or into the Kitchen? ")
if adv1 == "Upstairs":
    print("\nYou are now upstairs, you are standing at the beginning of a long hallway and you see two doors, a master bedroom and a washroom.")
    adv2 = input("Where do you want to go, the Master Bedroom or the Washroom? ")

    if adv2 == "Master Bedroom":
        print("\n You are now in the Master Bedroom and you see a large bed with a lump under the sheets and a closet with something glowing inside.")
        adv3 = input("Where do you want to go, the Bed or the Closet? ")
        if adv3 == "Bed": 
            print("Congrats you found a lump of money that Julian left for you! The end")
        elif adv3 == "Closet":
            print("You got caught by an evil Julian and he stole your glasses! The end")
            
    elif adv2 == "Washroom":
        print("\n You are now in the washroom and you see a toothbrush and a toilet")
        adv4 = input("Where are you using the Toothbrush or the Toilet? ")
        if adv4 == "Toothbrush":
            print("The toothbrush you used had squid ink on it and now your teeth are black! The end.")
        elif adv4 == "Toilet":
            print("You are about to flush the toilet when you realize the toilet paper is a roll of money! The end.")

elif adv1 == "Kitchen":
    print("\n You are now in the big luxurious kitchen! You see two stands to cook at the stove and the oven.")
    adv5 = input("Where do you want to go? The Stove or the Oven?")
    if adv5 == "Stove":
        print("\nYou are now at the stove and you see a large pot with a lid on it that smells amazing and a little moldy pan with some old scarmbled eggs on it.")
        adv6 = input("Which item do you want to use to cook with? The Large Pot or the Moldy Pan ")
        if adv6 == "Large Pot":
            print("Hurray you made the logical decision and you found a large pot of delicious chili and money stuck on the top of the lid! The end.")
        elif adv6 == "Moldy Pan":
            print("Why would you pick this? The food you cooked gave you poisoning and you spent the night on the toilet. The end.")
    
    elif adv5 == "Oven":
        print("\nYou are now at the oven where you see that there are two knobs to crank up the heat and cook the food faster and a knob to stop the cooking entirely.")
        adv7 = input("Which knob will you turn? The Cook or Off knob? ")
        if adv7 == "Cook":
            print("You cranked up the heat too high and all the money inside the oven burned to a crisp. The end")
        elif adv7 == "Off":
            print("Congrats you saved the money in the oven right before it burned to a crisp. The end")

print("")
print("")
print("")
print("Congrats if you made some money in Julian's Mansion! Either way, the cops will arrest you soon for trespassing.")