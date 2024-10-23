#Question 1 Five Marks - so easy its just one while and one for loop
x = 55
while x<=100:
    print(x)
    x+=1

for x in range(55,101,1):
    print(x)

#Question 2 Five Marks  - Ask user for three numbers in a loop and print the answer
count = 0
sum = 0
while count < 3:
    num = int(input("Whats your number?: "))
    sum += num
    count +=1

print(sum)

# Question 3 Ten Marks - Three options and each have different affect on dogs happiness and at the end u print the happiness level of dog
treats = 0
happy = 0
while treats < 5:
    what_treat = input("What treat")
    if what_treat == "Milk":
        happy += 1
        treats +=1
    elif what_treat == "Chew":
        happy += 3
        treats +=1
    elif what_treat == "Cream":
        happy += 5
        treats +=1
    else:
        print("Whats the treat bro")

if 0<= happy <=5:
    print("Dog is sad")
elif 6<= happy <=10:
    print("Dog is happy")
elif 11<= happy <=19:
    print("Dog is real happy")
elif 20<= happy <=25:
    print("Dog is too happy")