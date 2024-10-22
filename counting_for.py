print("Type in a message, and I'll display it five times.")

message = input("Message: ")

for n in range(1, 6, 1):
    print(f"{n}. {message}")
#The variable doesn't change the outcome of the code but the variable n could represent "number"
#The first arguements is just the range of where the numbers are in
#The second arguement is the increment in which the numbers go up in
#For a single number, the range goes under the input and to 0
#From range 3,9 it goes from 3 to 8
#Change to (0,10,1)
#(0,10,2)
