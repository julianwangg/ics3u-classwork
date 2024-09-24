store = "No Frills"
item = "Mangos"
price = 0.6
quantity = 19
subtotal = price * quantity
tax = subtotal * 0.13
total = tax + subtotal

#f string
print(f"At {store} I bought some {item}.")
#concatenation
print("They sold for $" + str(price) + " each.")
#dot format 
print("I wanted to purchase {} of them.".format(quantity))
print(f"The price without the tax will be ${subtotal}")
print(f"The tax added to the subtotal will be ${round(tax,2)}")
#f string was missing for this line which is why the total was not printed
print(f"The total price, with tax included, was ${round(total,2)}.")