# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


#import the random library
import random

# helper functions

def name_to_number(name):
    # convert name to number using if/elif/else
    if name == 'rock':
        choice_num = 0
    elif name == 'Spock':
        choice_num = 1
    elif name == 'paper':
        choice_num = 2
    elif name == 'lizard':
        choice_num = 3
    elif name == 'scissors':
        choice_num = 4
    else:
        choice_num = -1
        print "ERROR: Player choice " + name + " is not a valid option"
        
    # don't forget to return the result!
    return choice_num


def number_to_name(number):
    # delete the follwing pass statement and fill in your code below

    # convert number to a name using if/elif/else
    if number == 0:
        choice_name = 'rock'
    elif number == 1:
        choice_name = 'Spock'
    elif number == 2:
        choice_name = 'paper'
    elif number == 3:
        choice_name = 'lizard'
    elif number == 4:
        choice_name = 'scissors'
    else:
        choice_name = "ERROR"
        print "ERROR: Computer choice " + str(number) + " is not a valid option"
        
     # don't forget to return the result!
    return choice_name
    

def rpsls(player_choice): 
    # delete the follwing pass statement and fill in your code below
    
    # print a blank line to separate consecutive games
    print ""

    # print out the message for the player's choice
    print "Player chooses " + player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    #print player_number
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    #print comp_number

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice

    # compute difference of comp_number and player_number modulo five
    difference = (player_number - comp_number) %5

    # use if/elif/else to determine winner, print winner message
    if ( difference == 0 ):
        print "Player and Computer tie!"
    elif (difference == 1) or (difference == 2):
        print "Player wins!"
    else:
        print "Computer wins!"
    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
