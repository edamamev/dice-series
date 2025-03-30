
mDiceSet = {
    tuple(((1,0,0,0,0,0,0,0,0), 1.5, 0.5)),
    tuple(((0,1,0,0,0,0,0,0,0), 2, 1)),
    tuple(((0,0,1,0,0,0,0,0,0), 2.5, 1.5)),
    tuple(((0,0,0,1,0,0,0,0,0), 3, 2)),
    tuple(((0,0,0,0,1,0,0,0,0), 3.5, 2.5)),
    tuple(((0,0,0,0,0,1,0,0,0), 4.5, 3.5)),
    tuple(((0,0,0,0,0,0,1,0,0), 5.5, 4.5)),
    tuple(((0,0,0,0,0,0,0,1,0), 6.5, 5.5)),
    tuple(((0,0,0,0,0,0,0,0,1), 10.5, 9.5))
}

def DiceCalc(diceNum, diceSet):
    newDiceSet = set()
    for dice in diceSet:
        for diceVar in mDiceSet:
            newDiceSet.add(DiceSum(dice, diceVar))
    diceNum -= 1
    if (diceNum):
        youngDiceSet = DiceCalc(diceNum, newDiceSet)
        for roll in youngDiceSet:
            newDiceSet.add(roll)
    return newDiceSet
pass

# Combining Dice into a Roll
def DiceSum(diceA, diceB):
    return (
        # Dice that are Part of the Roll
        DiceTypeAddition(diceA[0], diceB[0]),

        # Expected Value of Roll
        diceA[1] + diceB[1],

        # Range of Rolls
        diceA[2] + diceB[2]
    )


def DiceTypeAddition(typesA, typesB):
    outTypes = [0,0,0,0,0,0,0,0,0]
    for i in range(9):
        outTypes[i] = typesA[i] + typesB[i]
    return tuple(outTypes)

def SortDiceByEX(diceSet):
    diceList = list(diceSet)
    for i in range(1, len(diceList)):
        a = diceList[i]
        # Move elements of diceList[0 to i-1],
        # which are greater to one position
        # ahead of their current position
        j = i - 1
        while j >= 0 and a[1] < diceList[j][1]:
            diceList[j + 1] = diceList[j]
            j -= 1
        diceList[j + 1] = a
    return diceList

def GetRollValues():
    diceInRoll = 10
    # 1 Dice Rolls
    rollSet = mDiceSet
    # 2 - `diceInRoll` Dice Rolls
    youngRollSet = DiceCalc(diceInRoll - 1, mDiceSet)
    for roll in youngRollSet:
        rollSet.add(roll)
    
    # Sorted List of Roll Values by Expected Value
    return SortDiceByEX(rollSet)

def RollsToString(rollList):
    output = ""
    for i in range(len(rollList)):
        output += "{},\n".format(rollList[i])
    return output

def Dices(rollList):
    for i in range(len(rollList)):
        rollList[i] = Dicify(rollList[i])
    return rollList

def Dicify(roll):
    return (("{}d2, {}d3, {}d4, {}d5, {}d6, {}d8, {}d10, {}d12, {}d20".format(roll[0][0], roll[0][1], roll[0][2], roll[0][3], roll[0][4], roll[0][5], roll[0][6], roll[0][7], roll[0][8])), roll[1], roll[2])

def Dice():
    rollList = GetRollValues()
    rollList = Dices(rollList)
    return RollsToString(rollList)

print(Dice())