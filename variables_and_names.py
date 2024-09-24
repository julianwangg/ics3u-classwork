# states the team name 
team = "Toronto Blue Jays"
# states the current date
current_date = "September 24 2024"
# states the player's name
player = "Vladmir Guerrero Jr"
# states the player's home runs
home_runs_to_date = 31
# states the games played by the player
games_played = 88
# states the total amount of season games
total_season_games = 162
# states the home run record
home_run_record = 73

# states the amount of unplayed games (= 162-88)
games_remaining = total_season_games - games_played
# states the player's home runs per game (31/88)
home_runs_per_game = home_runs_to_date / games_played
# states projected amount of home runs by the player (31/88 * 162)
projected_home_runs = home_runs_per_game * total_season_games
# states if the player can or cannot break the home run record (31/88 * 162 compared to 73)
can_break_record = projected_home_runs > home_run_record

print (f"{player} of the {team}")
print (f"currently has {home_runs_to_date} homeruns as of {current_date}.")
print (f"The current MLB record for most home runs in a season is {home_run_record}.")
print (f"With {games_remaining} games remaining and an average of {round(home_runs_per_game,2)}.")
print (f"it is {can_break_record} that he is on pace to break the record.")
print (f"{player} is projected to hit {round(projected_home_runs)} home runs this season.")
print ("The code has two empty lines in between each line to sort out each type of code in a specific manner so it is not clumped together. The variables are stated in the first cluster and the variables that need to be calculated are stated on the second. The third cluster contains the print function stating sentences and the numbers that correspond to them")
print ("I know that games_remaining must be correct because the amount of games remaining has to be the total games subtracted by the games already played.")