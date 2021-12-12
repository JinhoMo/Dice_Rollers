import random
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

scores = []

#110 Meter Hurdles
print(partition(middle = "110 Meter Hurdles"), partition(), """Throw all five dice, up to 6 times, until you are satisfied with the result.
The final score will be the total value of all five dice of the last attempt.""", partition(), sep = "\n")

final = 0
for i in range(6):
    rolls = roll(5)
    printDiceRoll(rolls, addInFront = "\n")
    final = sum(rolls)
    if i == 5:
        print("No more attempt remaining...")
        break
    user = input("Do you want to stop(please answer with yes or no)?\n")
    if user.lower() == "yes":
        break

scores.append(final)
print(partition(middle = "Gamed ended"), partition(), "\n", sep = "\n")

#Pole-Vault

print(partition(middle = "Pole Vault"), partition(), """Jumping starts at the height of 10 and is increased by 2 each turn.\nPlayers take turn for each height or can decide to skip it.
You have three attempts for each height.\nThrow two to eight dice to equal or exceeds the current height without any 1s.
The final socre will be the maximum height which was mastered.""", sep = "\n")

height = 10
nexth = 2
final = 0
while True:
    print(partition(), f"Current height is {height}.", sep = "\n")
    user = input('Would you like to have turn or skip it(please answer with "have" or "skip")?\n')
    if user.lower() == "skip":
        height += nexth
        print(partition())
        continue
    for i in range(3):
        result = 0
        rolls = []
        diceroll = 0
        while True:
            user = input("\nHow many dice do you want to roll from two to eight dice?\n")
            try:
                diceroll = int(user)
                if not diceroll <=  1 or diceroll >= 9:
                    break
                print("Invalid Move")
            except ValueError:
                print("Invalid Move")
        rolls = roll(diceroll)
        result = sum(rolls)
        TF = False
        printDiceRoll(rolls)
        if 1 in rolls:
            TF = True
            print("Dice roll has 1 included.")
        if result < height or TF:
            print(f"Faild.\n{'Please retry!!' if not i == 2 else ''}\n")
            continue
        print(f"Passed the height {height}")
        final = height
        break
    if not final == height:
        scores.append(final)
        break
    height += nexth
print(partition(middle = "Game Ended"), partition(), "\n", partition(middle = "Scores"), f"110 Meter Hurdles - {scores[0]}\nPole-Vault - {scores[1]}", sep = "\n")
