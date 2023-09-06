import pprint

compound = ["ingredient_name", "quantity", "measure"] # better to store it
# in a file
fileName = 'cookFiles//recipes.txt' # better to get it like a parameter while run
# the
# programm
def parcing_recipes(compound, lst):
    # create dict from lines of file
    tempDict = {}
    recipe = iter(lst.splitlines())
    recipe_title = next(recipe)
    compaundCount = int(next(recipe))
    while compaundCount:
        curLine = next(recipe).split(' | ')
        tempDict.setdefault(recipe_title, []).append(dict(zip(compound,
                                                              curLine)))
        compaundCount -= 1
    return tempDict

def fileRead(fileName):
    with open(fileName, 'r', encoding='utf-8') as myFile:
        fileData = myFile.read()
        cook_book = {}
    return fileData

def createCoocBook(recipesData):
    coocBook = {}
    for line in recipesData.split('\n\n'):
        coocBook.update(parcing_recipes(compound, line))
    return coocBook

def shopList(lst: list, PersonCount: int):
    dictIngredients = {}
    if PersonCount:
        for el in lst:
            for ingredients in cookBook[el]: # find dish in dictionary
                ingName = ingredients['ingredient_name']
                measure = ingredients['measure']
                quantity = ingredients['quantity']
                dictIngredients.setdefault(ingName, {}).setdefault('measure',
                                                                measure)
                dictIngredients[ingName]['quantity'] = (
                        dictIngredients.setdefault(ingName, {}).setdefault(
                            'quantity', 0) + int(quantity) * PersonCount)
        return dictIngredients
    return ("Looks like you'll be alone tonight. So take a beer and write "
            "some code or go to habrahabr ;)")


if __name__ == '__main__':
    print("let's start!")
    createCoocBook(fileRead(fileName))
    print()
    cookBook = createCoocBook(fileRead(fileName))
#    thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
    pprint.pprint(cookBook)

listDishes = ["Утка по-пекински", "Запеченный картофель"] # both of dishes
# contain honey
print("Choose dishes you want to cook (by default already added for 1 person: "
      "'Запеченный картофель', 'Омлет')\nRecipes in "
      "cookBook:")
print(*cookBook, sep=', ')
# print("Choose dishes you want to cook (by default already added for 1 person: "
#       "'Запеченный картофель', 'Омлет')\nRecipes in "
#       "cookBook:")
# can ask for more dishes
# inputDish = input("Add you dish")
# while inputDish in cook_book:
#     list_cook.append(answer)
#     inputDish = input("one more? ")
# else:
#     print("sorry, there is no recipe for this in cookBook")
personCount = int(input("Enter count of persons: "))
print("\nLet's go shopping:\n")
pprint.pprint(shopList(listDishes, personCount))
