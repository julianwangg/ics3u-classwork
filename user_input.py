print("Enter the following information about an item you wish to purchase..")
print()

print("The name of the item:")
name = input(("Enter the name of the item:"))
price = float(input("The price: $"))
quantity = int(input("How many would you like?"))

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")

#1 Price required a number whilst name required a word response. The spread between two lines and one was also put into just one line
#3 A prompt is a question. Switching the order of the items causes an issue because you are not taking any input beforehand.
#4 Int stores it as a number and float stores it as a decimal number. Without it, this would store a string and fail to work.