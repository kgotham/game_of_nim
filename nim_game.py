#Ksusha Gotham
#Complete a game of Nim where the computer always wins, the goal is to get user inputs until no chips are left and the game ends.

import time
import doctest

def initializeGame():
    """   void -> int
    PRE:  Nothing is passed to this function
    POST: A valid number of chips is returned
    """
    validChips = 0
    while validChips<=0:
        validChips = int(input("Enter a positive number of chips. "))
        if validChips<=0:
            print("Oops! You can't start with zero or less chips.")
            print("Please try again.")
    return validChips
# end of initializeGame

def displayPiles(pile1, pile2):
    """   int,int -> void
    PRE:  Two non-negative integers are passed to the function
    POST: The piles of chips are displayed to the screen where each
          chip is an "O".  A space inserted after every fifth chip to
          improve readability. Further, a newline is inserted after
          both piles are displayed
    >>> displayPiles(3,6)
    Pile 1: OOO
    Pile 2: OOOOO O
    <BLANKLINE>
    >>> displayPiles(6,4)
    Pile 1: OOOOO O
    Pile 2: OOOO
    <BLANKLINE>
    >>> displayPiles (0,20)
    Pile 1:
    Pile 2: OOOOO OOOOO OOOOO OOOOO
    <BLANKLINE>
    >>> displayPiles (100,100)
    Pile 1: OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO
    Pile 2: OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO
    <BLANKLINE>
    """
    
    print('Pile 1:',end='')
    for c in range(0,pile1):
        if c%5 == 0:
            print(" ",end = '')
            pass
        print('O',end = '')
    print('\n',end='')
    print('Pile 2:',end = '')
    for c in range(0, pile2):
        if c%5 == 0:
            print(" ", end='')
            pass
        print('O', end='')
    print('\n',end='')
    print()
# end of displayPiles 

def getHumanMove(p1chips, p2chips):
    """   int,int -> int,int
    PRE:  Two integers, both non-negative, at least one larger than zero, are passed in.  The
          first number represents the count of chips in pile 1, the second number is the count of
          chips in pile 2
    POST: Two values are returned: (1) the pile that the human player has chosen (e.g. 1 or 2)
          which I'll call humanPile. (2) the number of chips that the human would like to take
          from his chosen pile which I'll call humanChips.  The function ensures that the move is
          valid but does not update the number of chips in either pile.
          To be precise, upon returning the function ensures that there are at least
          humanChips chips left in humanPile.   
    """
    reqMove = "You must take atleast one chip."
    numPile = int(input("Which pile would you like to take from? (1 or 2)"))
    if numPile == 1:
        numChips1 = int(input("How many would you like from pile 1? "))
        if numChips1 <= p1chips and numChips1 != 0:
            print("That was a legal move. Thank you.")
            return numPile, numChips1
        elif numChips1 == 0:
            print("\n",reqMove,"\n")
            getHumanMove(p1chips,p2chips)
        else:
            print("Pile 1 does not have that many chips. Try again.")
            getHumanMove(p1chips, p2chips)
    elif numPile == 2:
        numChips2 = int(input("How many would you like from pile 2? "))
        if 0<numChips2 <= p2chips and numChips2 != 0 :
            print("That was a legal move. Thank you.")
            return numPile, numChips2
        elif numChips2 == 0:
            print('\n',reqMove,'\n')
            getHumanMove(p1chips,p2chips)
        else:
            print("Pile 2 does not have that many chips. Try again.")
            getHumanMove(p1chips, p2chips)
    else:
        if numPile != 1 or numPile != 2:
            print(numPile, "is not a valid pile number")
            getHumanMove(p1chips, p2chips)
    return p1chips,p2chips

# end of getHumanMove  

def updatePiles(pileChosen, chipsChosen, pile1chips, pile2chips):
    """   int, int, int, int -> int, int
    PRE:  Four parameters are passed to this function. (1) the pile chosen from, (2) the
          number of chips chosen from that pile, (3) the current count of chips in pile 1, (4) the
          current count in pile 2.
    POST: Two values are returned, namely, the count of chips in each pile after the human moves.
    >>> updatePiles(1,3,5,6)
    (2, 6)
    >>> updatePiles(2,3,5,6)
    (5, 3)
    >>> updatePiles(1,5,7,9)
    (2, 9)
    >>> updatePiles(2,12,24,30)
    (24, 18)
    """
    if pileChosen == 1:
        pile1chips = pile1chips - chipsChosen
    if pileChosen == 2:
        pile2chips = pile2chips - chipsChosen
    return pile1chips, pile2chips
#end of updatePiles

def computerMove(humanPile, humanChips, pile1chips, pile2chips):
    """   int, int, int, int -> int, int
    PRE:  Four parameters are passed to this function: (1) the pile the human chose from on her
          last turn, (2) the number of chips the human took on her last turn, (3) the count of chips
          in pile 1, (4) the count of chips in pile 2.
    POST: the pile chosen by the computer, the number of chips chosen by the computer
    >>> computerMove(1,3,5,8)
    (2, 3)
    >>> computerMove(2,4,7,3)
    (1, 4)
    >>> computerMove(2,1,3,4)
    (1, 1)
    >>> computerMove(1,12,1,13)
    (2, 12)
    """
    if humanPile == 1:
        computerPile = 2
    elif humanPile == 2:
        computerPile = 1
    return computerPile, humanChips

#end of computerMove  ###########

### MAIN PROGRAM ################

if __name__ == '__main__':
    doctest.testmod()


print ("Welcome to the game of chips.  I know you know the rules so let's go.\n")

numChips = initializeGame()

pile1chips = numChips
pile2chips = numChips
gameOver = False

while not gameOver:
    print("Here are the piles ")
    displayPiles(pile1chips, pile2chips)
    print ("It is your turn.")    

    humanPile, humanChips = getHumanMove(pile1chips, pile2chips)
    pile1chips, pile2chips = updatePiles(humanPile, humanChips, pile1chips, pile2chips)
    print("Here are the piles ")
    displayPiles(pile1chips, pile2chips)
   
    computerPile, computerChips = computerMove(humanPile, humanChips, pile1chips, pile2chips)
    pile1chips, pile2chips = updatePiles(computerPile, computerChips, pile1chips, pile2chips)
    print ("Now it is my turn. I'm thinking ...")
    time.sleep(3)    #This is just to slow things down a little for readability by the human player.  
    print ("I, the champion chips computer, will take", computerChips, "chips from pile", computerPile)
    if pile1chips == 0 and pile2chips == 0:
        gameOver = True

print ("The game is over and I won because I took the last chip.")
print ("Thanks for playing.  You wanna wager next time?")

# for initialize game it was quite easy to test, since we didn't have to worry about inputs of string types. I just tested numbers greater than 0 and less than zero (and 0)
# for getHumanMove to be honest i still haven't figured out how to fix it completely but was to afraid to ask for help which is my own fault, sonmething about it isn't going through when
#i create an intetional error and it's saying computerPile is used before it is referenced. Anyways, the way I tested this was created chunks of numbers, (negative, zero, positive, more than 10, etc)
#and pretty much stress-tested it and fixed errors along the way until they (mostly) stopped...