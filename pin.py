PIN = "12345"

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")


print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")

#while is similar to if in the sense that they both detext if the statement is true before doing a task
#while is different because it can run forever until something happens
#an infinite loop occurs because there is no entry again after the wrong attempt so the loop just keeps repeating the same words