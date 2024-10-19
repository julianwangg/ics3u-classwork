import random
print("Here comes the dice!")
dices_rolled = 0
dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
while dice_1 != dice_2:
    print(f"Dice 1 : {dice_1}")
    print(f"Dice 2 : {dice_2}")
    sum = dice_1 + dice_2
    print(f"Sum: {sum}")
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)

print(f"Dice 1 : {dice_1}")
print(f"Dice 2 : {dice_2}")
sum = dice_1 + dice_2
print(f"Sum: {sum}")