robot_location = 40
ball_location = 45
goal_location = 30
have_ball = False

#Indicates to the player where you are in correlation to the ball
if robot_location < ball_location:
    print("Almost at the ball")

#Indicates to the player that you have went too far and need to go back
if robot_location > goal_location:
    print("You are beyond the goal.")

#Indicates to the player that the robot is at the goal
if robot_location == goal_location:
    print("The robot is at the goal.")

robot_location += 5

#Indicates to the player that the robot is at the goal after moving forward 5 units
if robot_location == goal_location:
    print("At the goal.")

#Indicates to the player that they are at the ball after moving forward 5 units
if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 15

#Indicates to the player that they have moved forwards too much
if robot_location < goal_location:
    print("You went too far.")

#Indicates to player that they have scored a goal
if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False

    #The purpose of an if statement is for the program to understand what to do in the case of certain situations. Any code that is indented after the if condition is part of the block and if the condition is true then the code will be executed
    # += adds a value to the variable and puts that value back in the variable
    # -= subtracts a value to the variable and puts that value back in the variable
