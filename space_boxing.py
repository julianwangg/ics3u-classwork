input("Hello Julio Cesar Chavez Mark VII!")
earth_weight = int(input("How much do you weigh on Earth in pounds? "))

print("Okay Julio, I hear you are a space boxer. We will discover your weight class at the planet you are going to!")
print("I have information of these six planets:   1. Venus   2. Mars    3. Jupiter  4. Saturn  5. Uranus  6. Neptune")
planet_visiting = int(input("Where are you boxing? "))

venus_weight = earth_weight * 0.78
mars_weight = earth_weight * 0.39
jupiter_weight = earth_weight * 2.65
saturn_weight = earth_weight * 1.17
uranus_weight = earth_weight * 1.05
neptune_weight = earth_weight * 1.23

if planet_visiting == 1: 
    print(f"Your weight on Venus is {venus_weight}lb!")
elif planet_visiting ==2:
    print(f"Your weight on Mars is {mars_weight}lb!")
elif planet_visiting ==3:
    print(f"Your weight on Jupiter is {jupiter_weight}lb!")
elif planet_visiting ==4:
    print(f"Your weight on Saturn is {saturn_weight}lb!")
elif planet_visiting ==5:
    print(f"Your weight on Uranus is {uranus_weight}lb!")
elif planet_visiting ==6:
    print(f"Your weight on Neptune is {neptune_weight}lb!")
else: print("Sorry Julio, that's not a valid planet, please choose from the index I have given you")

weight_division = float(input("Tell me what your weight is on your planet in pounds to get a weight class! "))
if 0<=weight_division<=115:
    print("Dang, be safe out there! One strong gust and you're out! your weight class is: FLYWEIGHT!")
elif 116<=weight_division<=154: 
    print("Not too bad! you are still a pretty gentle looking fella! Your class is: LIGHTWEIGHT!")
elif 155<=weight_division<=168: 
    print("Yikes! not too close! you are starting to get heavy! Your class is: MIDDLEWEIGHT!")
elif 169<=weight_division<=999: 
    print("YIKES! YOU ARE ONE BIG BUFF BOXER! Your class is: HEAVYWEIGHT!")
else: print("You are too heavy! are you even alive still??")