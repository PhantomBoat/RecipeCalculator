def GetString():
    return


def VerifyChoice(choice, options):
    upperChoice = choice.upper()
    upperOptions = []

    for option in options:
        upperOptions.append(str(option).upper())

    return upperChoice in upperOptions


def VerifyChoiceInt(choice: any, options: list[int]) -> bool:
    intChoice = -1
    try:
        intChoice = int(choice)
    except:
        return False

    return intChoice in options


def IndexOfOption(choice, options):
    upperChoice = choice.upper()
    upperOptions = []

    for option in options:
        upperOptions.append(str(option).upper())

    return upperOptions.index(upperChoice)


def IndexOfOptionInt(choice: int, options: list[int]) -> int:
    return options.index(int(choice))


def GetValidChoice(validChoices, typeInt: bool) -> int:
    notValidChoice = True
    while notValidChoice:
        userChoice = input("Choose and option: ")
        if typeInt:
            if VerifyChoiceInt(userChoice, validChoices):
                return IndexOfOptionInt(userChoice, validChoices)
            else:
                print("Not a valid choice, pick again")
        else:
            if VerifyChoice(userChoice, validChoices):
                return IndexOfOption(userChoice, validChoices)
            else:
                print("Not a valid choice, pick again")


def GetExistingOrNew(existingChoices):
    indexes = [*range(1, len(existingChoices))]
    indexes.append(len(existingChoices))
    indexes.append(0)
    existingChoices.append("New entry")
    PrintVerticalMenu(existingChoices, indexes)
    return GetValidChoice(indexes, True)


def PrintVerticalMenu(menuItems, indexes):
    if len(menuItems) == 0:
        return

    for i in range(0, len(menuItems)):
        print(str(indexes[i]) + ": " + menuItems[i])


def PrintHorizontalMenu(menuItem, indexes):
    printStr = ""
    index = 0
    for item in menuItem:
        printStr = printStr + " " + indexes[index].upper() + ") " + item
        index = index + 1
    print(printStr)

def AnythingBut(notAllowed: list[any], query: str) -> any:
    userInput = ""
    alreadyExits = True
    while alreadyExits:
        userInput = input(query)
        alreadyExits = userInput in notAllowed
    return userInput