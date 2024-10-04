print("Hey you! Come take my quiz to win a prize!")
name = input("Alright to start off, what is your name? ")
score = 0

response_1 = input(f"Okay {name}, are you ready to take this quiz to win a prize? ")
if response_1 == "yes":
    print("Alright lets get started!")
elif response_1 == "no":
    print("Too bad, lets get started!")
else: print("I'm not sure what you said but lets get started anyways!")

print("Question Number One: What are the names of Mars' moons?")
answer_question_one = int(input("1) Deimos and Phobos 2) Mars 1XC-90 and Mars 2XC-80 3) Demetrius and Pheobe" ))
if answer_question_one == 1:
    print("Yay you got the right answer!")
    score +=1
else: print("Wrong, Okay that one was a bit hard, ill ease up next question")

print("Question Number Two: What is the electronegativity of the most electronegative element on the periodic table?")
answer_question_two = int(input("1) 4.0 2) 5.0 3) 4.5"))
if answer_question_two == 1:
    print("Yay you got it right again!")
    score+=1
else: print("What do you mean that's hard, should have paid attention in chemistry class!")

print("Final Question: What is my favourite food?")
answer_question_three = int(input("1) Sushi 2) Baconator 3) Mangos"))
if answer_question_three == 1:
    print("Dang, you got this one right?? Nice job!")
    score+=1
else: print("Should've known me better...")


if score==1:
    print("No prize for you, you failed the test!")
elif score>1: print(f"Hurray! this was your score: {score}/3! And for your prize, here is a happy face :)")