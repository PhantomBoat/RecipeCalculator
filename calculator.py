import json
import getUserInput
import formatJson


recipesPath = "recipes.json"

recipesFile = open(recipesPath)
settingsFile = open("settings.json")
conversionFile = open("conversions.json")

recipes = json.load(recipesFile)
settings = json.load(settingsFile)
conversions = json.load(conversionFile)


def GetCategory():
    getUserInput.GetExistingOrNew()


def MainMenu():
    getUserInput.PrintHorizontalMenu(mainMenu, mainMenuIndex)
    choiceIndex = getUserInput.GetValidChoice(mainMenuIndex, False)
    #choiceIndex = 0
    if choiceIndex == 0:
        Categories()
    elif choiceIndex == 1:
        AddRecipe()
    elif choiceIndex == 2:
        AddConversion()
    elif choiceIndex == 3:
        OpenSettings()


def AddRecipe():
    print("Not implemented")


def AddConversion():
    print("Not implemented")


def OpenSettings():
    print("Not implemented")


def Categories():
    categories = recipes["categories"]
    choiceIndex = getUserInput.GetExistingOrNew(categories)

    if choiceIndex + 1 == len(categories):
        NewCategory()


def NewCategory():
    global recipes, recipesPath

    categories = recipes["categories"]
    print("Create category")
    newCategory = getUserInput.AnythingBut(
        categories, "Name of new category: ")

    # Removes the "new entry" from the list
    categories.pop()
    categories.append(newCategory)
    WriteDataToFile(recipes, recipesPath)


def WriteDataToFile(data: dict, filePath: str):
    with open(filePath, 'w', encoding="utf-8") as file:
        json.dump(data, file)


mainMenu = ["choose category", "add recipe", "add conversion", "open settings"]
mainMenuIndex = ["c", "r", "a", "s"]


def SanityCheck():
    if len(mainMenu) != len(mainMenuIndex):
        exit(1)


def Main():
    SanityCheck()
    MainMenu()
    # Categories()


Main()
