
master_dice_set = {
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


def DiceCalc(dice_number, dice_set):
    new_dice_set = set()
    for dice in dice_set:
        for dice_var in master_dice_set:
            new_dice_set.add(DiceSum(dice, dice_var))
    dice_number -= 1
    if (dice_number):
        young_dice_set = DiceCalc(dice_number, new_dice_set)
        for roll in young_dice_set:
            new_dice_set.add(roll)
    return new_dice_set
pass


# Combining Dice into a Roll
def DiceSum(dice_A, dice_B):
    return (
        # Dice that are Part of the Roll
        DiceTypeAddition(dice_A[0], dice_B[0]),

        # Expected Value of Roll
        dice_A[1] + dice_B[1],

        # Range of Rolls
        dice_A[2] + dice_B[2]
    )


def DiceTypeAddition(dice_types_A, dice_types_B):
    output_dice_types = [0,0,0,0,0,0,0,0,0]
    for i in range(9):
        output_dice_types[i] = dice_types_A[i] + dice_types_B[i]
    return tuple(output_dice_types)


def SortDiceByEX(dice_set):
    dice_list = list(dice_set)
    for i in range(1, len(dice_list)):
        a = dice_list[i]
        # Move elements of diceList[0 to i-1],
        # which are greater to one position
        # ahead of their current position
        j = i - 1
        while j >= 0 and a[1] < dice_list[j][1]:
            dice_list[j + 1] = dice_list[j]
            j -= 1
        dice_list[j + 1] = a
    return dice_list


def GetRollValues():
    number_of_dice_in_roll = 10
    # 1 Dice Rolls
    roll_set = master_dice_set
    # 2 - `diceInRoll` Dice Rolls
    young_roll_set = DiceCalc(number_of_dice_in_roll - 1, master_dice_set)
    for roll in young_roll_set:
        roll_set.add(roll)
    
    # Sorted List of Roll Values by Expected Value
    return SortDiceByEX(roll_set)


def RollsToString(list_of_rolls):
    output = ""
    for i in range(len(list_of_rolls)):
        output += "{},\n".format(list_of_rolls[i])
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