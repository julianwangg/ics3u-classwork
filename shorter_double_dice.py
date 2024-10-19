import random
print("Here comes the dice!")

while True:
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    print(f"Dice 1 : {dice_1}")
    print(f"Dice 2 : {dice_2}")
    print(f"Sum: {dice_1 + dice_2}")
    if dice_1 == dice_2:
        break