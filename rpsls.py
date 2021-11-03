import random
import time
items = ["rock","paper","scissors","lizard","spock"]
score = 0
win = 0
lose = 0
tie = 0
 
print("You can check your score at any time by typing 'Score' You can also exit the system by typing 'Quit'.")
print("Have fun playing Rock Paper Scissors Lizard Spock :)")
print("")
time.sleep(1)
loop = False
while loop == False:
    comp = random.choice(items)
    player = input("Pick Rock, Paper, Scissors, Lizard, Spock ")
    print("")
    player = player.lower()
    
    #--Tie--#
    if player == comp:
        print("Tie")
        score = score +0.5
        tie = tie +1
        
        
     #--Player Picks Rock--#
    elif player == "rock":
        if comp == "scissors":
            print("You win, rock crushes scissors ")
            score = score +1
            win = win +1

        elif comp == "lizard":
            print("You win, rock crushes lizard")
            score = score +1
            win = win +1

        elif comp == "paper":
            print("You lose, paper covers rock")
            score = score -1
            lose = lose +1
        elif comp == "spock":
            print("You lose, spock vaporizes rock")
            score = score -1
            lose = lose +1
        else:
            print("Error")

    #--Player Picks Paper--#
    elif player == "paper":
        if comp == "rock":
            print("You win, paper covers rock")
            score = score +1
            win = win +1

        elif comp == "spock":
            print("You win, paper disproves spock")
            score = score +1
            win = win +1

        elif comp == "scissors":
            print("You lose, scissors cuts paper")
            score = score -1
            lose = lose +1

        elif comp == "lizard":
            print("You lose, lizard eats paper")
            score = score -1
            lose = lose +1

        else:
            print("Error")
        
    #--Player Picks Scissors--#
    elif player == "scissors":
        if comp == "paper":
            print("You win, scissors cuts paper")
            score = score +1
            win = win +1

        elif comp == "lizard":
            print("You win, scissors decapitates lizard")
            score = score +1
            win = win +1

        elif comp == "rock":
            print("You lose, rock crushes scissors")
            score = score -1
            lose = lose +1

        elif comp == "spock":
            print("You lose, spock smashes scissors")
            score = score -1
            lose = lose +1

        else:
            print("Error")

    #--Player Picks Lizard--#
    elif player == "lizard":
        if comp == "paper":
            print("You win, lizard eats paper")
            score = score +1
            win = win +1

        elif comp == "spock":
            print("You win, lizard poisons spock")
            score = score +1
            win = win +1

        elif comp == "rock":
            print("You lose, rock crushes lizard")
            score = score -1
            lose = lose +1

        elif comp == "scissors":
            print("You lose, scissors decapitates lizard")
            score = score -1
            lose = lose +1

        else:
            print("Error")

    #--Player Picks Spock--#
    elif player == "spock":
        if comp == "scissors":
            print("You win, spock smashes scissors")
            score = score +1
            win = win +1

        elif comp == "rock":
            print("You win, spock vaporizes rock")
            score = score +1
            win = win +1

        elif comp == "paper":
            print("You lose, paper disproves spock")
            score = score -1
            lose = lose +1
            
        elif comp == "lizard":
            print("You lose, lizard poisons spock")
            score = score -1
            lose = lose +1

        else:
            print("Error")

    #--Player Picks Score--#
    elif player == "score":
        print("Your total number of points is",score)
        print("You won",str(win), "times, lost",str(lose), "times and tied",str(tie), "times")
        print("")
        time.sleep(1)

        #--Ask the user to continue--#
        loop2 = True
        while loop2 == True:
            con = input("Would you like to continue y or n? ")
            con = con.lower()
            if con == "y":
                loop2 = False
                

            elif con == "n":
                print("Thank you for playing, ending program")
                quit()
            else:
                print("invalid input")
                loop2 = True
        
    
    #--Player Picks Quit--#
    elif player == "quit":
        print("Thank you for playing, ending program")
        quit()
    
    #--User incorrect input--#
    else:
        print("This is not valid")