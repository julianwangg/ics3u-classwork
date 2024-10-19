count = 0
wins = 0
losses = 0
while count < 6:
    result = input("Enter result (W or L): ")
    count += 1

    if result == "W":
        wins +=1
    elif result == "L":
        losses +=1

ratio = wins / losses
print(f"The win/loss ratio for your team is {ratio}")