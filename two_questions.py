print("TWO QUESTIONS")
print("You think of an object and I will try and guess it!")

object = input("Question 1) Is it an animal, vegetable or mineral? ")

if object == "animal": 
    size = input("Is it bigger than a breadbox? ")
    if size == "yes":
        print("I think your object is a moose!")
    if size == "no":
        print("I think your object is a squirrel!")
   
if object == "vegetable":
    size = input("Is it bigger than a breadbox?")
    if size == "yes":
        print("I think your object is a cabbage!")
    if size == "no":
        print("I think your object is a carrot!")
    
if object == "mineral": 
    size = input("Is it bigger than a breadbox? ")
    if size == "yes":
        print("I think your object is a camaro!")
    if size == "no":
        print("I think your object is a paperclip!")