print("Wanna know if your triangle is a right one?")

side1 = int(input("Side 1: "))
side2 = int(input("Side 2: "))

while side2 < side1:
    print(f"{side2} is smaller than {side1}. try again.")
    side2 = int(input("Side 2: "))

while True:
    side3 = int(input("Side 3: "))
    if side3 >= side2:
        break
    else:
        print(f"{side3} is smaller than {side2}. try again.")
    
print(f"Your three sides are {side1}, {side2}, {side3}")
if side1 ** 2 + side2 ** 2 == side3 ** 2:
    print("These sides make a right triangle yay")
else: print("Not a right triangle unfortunately!")