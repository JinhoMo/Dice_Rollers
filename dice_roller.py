import random
import time
scores = {}
update = scores.update
def dice() -> int:
    """Return an random integer value."""
    return random.randint(1, 6)

def roll(num : int) -> list:
    """Return the list value of inputed number of random integer."""
    return [dice() for i in range(num)]

def getDiceFace(index : int) -> str:
    """Return each dice face accordingly to the inputed integer.\nEX) 1 >> \"⚀\"\nThe input should be 1 to 6."""
    return {1 : u"\u2680", 2 : u"\u2681", 3 : u"\u2682", 4 : u"\u2683", 5 : u"\u2684", 6 : u"\u2685"}.get(index, None)

def listDiceFace(lis : list) -> list:
    '''Return each Dice Face list accordingly to the inputed list.\nEX) [1, 2, 3] >> ["⚀", "⚁", "⚂"]'''
    return [getDiceFace(i) for i in lis]

def printDiceRoll(diceRoll : list, addInFront = '', addInBack = '') -> None:
    """Print both Dice Roll list and Dice Face list.\nEX) Result : ⚀, ⚁, ⚂ (It's 1, 2, 3)"""
    print(f'{addInFront}Result : {", ".join(listDiceFace(diceRoll))} (It\'s {", ".join(map(str, diceRoll))}){addInBack}')

def partition(symbol = "-", length = 77, middle = "") -> str:
    """Return partition that made of inputed length, inputed symbol and middle if it inputed."""
    length -= len(middle) + 2
    p = (lambda s, l: s * (l // 2))(symbol, length)
    return symbol * length if middle == "" else f"{p} {middle} {p}"

def gameEnded():
    """Print Game end message"""
    print(partition(middle = "Gamed ended"), partition(), "\n", sep = "\n")

def gameStart(name, ex):
    """Print the header and game explanation"""
    print(partition(middle = name), partition(), ex, partition(), sep = "\n")

def gameScores(*names):
    """Print the entire score board"""
    global scores
    print(partition(middle = "Scores"), partition(), sep = "\n")
    for k, v in scores.items():
        print(f"{k} : {v}")

def meters_100_sum(lis, num = 6):
    return sum(lis) - (lis.count(num) * num * 2)

def meters_100():
    #100 Meters
    game = "100 Meters"
    gameStart(game, "Throw the first four dice until you are satisfied with the result.\nThen throw the other four dice and proceed in the same manner.\nYou have a maximum of seven throws for both sets.\nFor examle, if you throw six times in frist set, only 1 attempt will remain for next set.\nThe final scoring will be the total value of the dice, but 6s count negative.")
    
    #setting vairables
    final = 0
    nextset = False
    attempt = []
    slep = time.sleep
    append = attempt.append
    TF = False
    
    #give user seven attempts
    for i in range(7):

        #indicate the set
        print(f"\nYou are in {'first' if not nextset else 'second'} set.")

        #automatic move set logic
        if i == 5 and not nextset:
            print("This is last attempt in first set. The program will automatically move to next set")
            slep(3)
            TF = True
        elif i == 7:
            print("The last attempt")
            slep(3)
        rolls = roll(4)
        total = meters_100_sum(rolls)
        printDiceRoll(rolls, addInFront = "\n", addInBack = f"\nTotal : {total}")

        #recording the score of each attempts
        if TF:
            append(total)
            nextset = True
            continue
        elif nextset and i == 6:
            append(total)
            break

        #asking user to continue the attempts
        user = input("Are you satisfied(Please answer with yes or no)?\n")
        if user.lower() == "yes" and not nextset:
            append(total)
            nextset = True
        elif user.lower() == "yes" and nextset:
            append(total)
            break
    
    #buffer
    slep(2)

    #record final score & game ends
    final = sum(attempt)
    gameEnded()
    return {game : final}

def meterHurdles_110():
    #110 Meter Hurdles
    game = "110 Meter Hurdles"
    gameStart(game, "Throw all five dice, up to 6 times, until you are satisfied with the result.\nThe final score will be the total value of all five dice of the last attempt.")
    
    #score vairable
    final = 0

    #give 6 attempts
    for i in range(6):

        #dice rolls
        rolls = roll(5)
        printDiceRoll(rolls, addInFront = "\n")

        #update the final score
        final = sum(rolls)

        #indicate/asking user about the attempts
        if i == 5:
            print("No more attempt remaining...")
            break
        user = input("Do you want to stop(please answer with yes or no)?\n")
        if user.lower() == "yes":
            break
    
    gameEnded()
    return {game : final}
    
def longJump():
    # final = 
    #Long Jump
    game = "Long Jump"
    gameStart(game, "Start with five dice.\nYou must freeze at least one die at each throw.\nInvalid if forzen dice total is 9 or more.\nStart with frozen dice.\nYou must freeze at least one die at each throw.\nYou have three attempts.\nThe final score will be best total value of all dice forzen in jump")
    
    return {game : final}

def shotPut():
    #Shot Put
    game = "Shot Put"
    gameStart(game, """Throw one die after the other.\nYou can decide to score at any time.\nIf you throw a 1 you suffer an invalid attempt.\nYou have three attempts.\nThe final score will be the highest score of all three attempts.""")
    
    # score collecting vairable
    subscores = []
    
    #Play round for 3 times, each round can be identify as i + 1
    for i in range(3):
        print(f"Attempt {i + 1}:")
        score = 0

        #8 times of attempts
        for j in range(8):

            #dice roll & print
            rolls = roll(1)
            printDiceRoll(rolls)

            #game logic, if roll is 1, fail the game(give 0)
            if 1 in rolls:
                score = 0
                break

            #record socre of the attempt
            score += rolls[0]

            #asking to continue
            user = input("Want to continue(Please answer with yes or no)?\n")
            if user.lower() == "no":
                break

        #print final score
        print(f"The final score of this attempt is {score}.\n")

        #record score of the round
        subscores.append(score)

    #record score of the game
    final = max(subscores)
    gameEnded()
    return {game : final}


def poleVault():
    #Pole-Vault
    game = "Pole Vault"
    gameStart(game,"""Jumping starts at the height of 10 and is increased by 2 each turn.\nPlayers take turn for each height or can decide to skip it.\nYou have three attempts for each height.\nThrow two to eight dice to equal or exceeds the current height without any 1s.\nThe final socre will be the maximum height which was mastered.""")
    
    #inital variables
    height = 10
    nexth = 2
    final = 0
    while True:

        #explain current height & asking for have the chance or not.
        print(partition(), f"Current height is {height}.", sep = "\n")
        user = input('Would you like to have turn or skip it(please answer with "have" or "skip")?\n')
        if user.lower() == "skip":
            height += nexth
            continue
        print()

        #run for 3 attempts
        for i in range(3):

            #system record vairable
            result = 0
            rolls = []
            diceroll = 0
            while True:

                #asking for number of dice roll
                user = input("How many dice do you want to roll from two to eight dice?\n")
                try:

                    #get dice rolls
                    diceroll = int(user)

                    #in case of invalid rolls, stop the user from doing it
                    if not (diceroll <=  1 or diceroll >= 9):
                        break
                    print("Invalid Move")
                except ValueError:
                    print("Invalid Move")

            #roll the inputed number of dicerolls
            rolls = roll(diceroll)
            result = sum(rolls)
            TF = False

            #show the dice rolls and give the score or event accordingly to the game logic
            printDiceRoll(rolls)
            if 1 in rolls:
                TF = True
                print("Dice roll has 1 included.")
            if result < height or TF:
                print(f"Faild.{'Please retry!!' if not i == 2 else ''}\n")
                continue
            print(f"Passed the height {height}")
            
            #record / reset final score
            final = height
            break

        #check user passed the height
        if not final == height:
            scores[game] = final
            break
        height += nexth
    gameEnded()
    return {game : final}

#call games
update(meters_100())
update(meterHurdles_110())
update(shotPut())
update(poleVault())

#print game score
gameScores()
