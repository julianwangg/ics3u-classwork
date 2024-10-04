team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
elif team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
if team_b_wins > team_a_wins:
    print("Team B has more wins than Team A.")
else:
    print("Both Teams A and B have the same number of wins.")

#The code outputs that both teams have the same amount of wins because it first calculates the score of the current game that Team A won, then, it reads the code under that which tells it to state which team has more wins in which the score is tied because of the previous game.
#The elif and else statements are creating seperate backup scenarios in the case that the if statement is not true so that there is other options to output for different inputs.
#By changing the elif to if, it makes the block seperate which makes them run seperately even if it is not intended to.