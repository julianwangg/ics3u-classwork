name = input("Whats your name? ")
age = int(input(f"hello {name}, how old are you? "))
if age <16:
    print("you can't drive yet!")
if age <18:
    print("you can't vote yet!")
if age <19:
    print("you can't drink yet!")
if age ==16:
    print(f"you can start driving {name}")
if age ==18:
    print(f"you can start voting {name}")
if age ==19:
    print(f"you can start drinking {name}")
if age >=21:
    print(f"congrats {name}! you can do anything legal now!")


#Test plan
#Input              Processing                  Output
#15                 age<16 age<18 age<21        "you can't drive yet!, you can't vote yet!, you can't drink yet!"
#16                 age == 16               "you can start driving {name}""
#17                 age<18 age<21        "you can't vote yet!, you can't drink yet!"
#18                 age<21 age == 18       "you can start voting {name}, you can't drink yet!""
#19                 age<21 age == 19       you can start drinking {name}"
#21                 age>=21        "congrats {name}! you can do anything legal now!"