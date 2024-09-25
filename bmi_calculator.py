inch_height = float(input("How tall are you in inches?"))
pound_weight = float(input("How heavy are you in pounds?"))
feet_height = inch_height / 12
meter_length = inch_height / 39.37
kilo_weight = pound_weight * 0.453592
BMI_calculated_height = meter_length * meter_length
BMI = kilo_weight / BMI_calculated_height

print ("Your stats")
print (f"You are {feet_height} feet tall or {inch_height} inches tall")
print (f"And you are {kilo_weight}kg heavy.")
print (f"Your BMI is... {BMI}")