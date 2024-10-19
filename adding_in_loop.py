number = 0
print("Give me numbers and i will add em up")
input_num = int(input("Give me a number: "))
while input_num > 0:
    number += input_num
    print (f"The sum so far is {number}")
    input_num = int(input("Give me a number: "))

print(f"The final sum is {number}")