from datetime import date

class Recipe(object):

    def __init__(self, recipeName, author):
        self.recipe_name = recipeName
        self.recipe_author = author
        self.last_updated_by = author
        self.date_created = date.today()
        self.last_updated_on = date.today()
        self.servings = 0
        self.ingredients = {}
        self.items = []
        self.instructions = []
    
    def getRecipeName(self):
        return self.recipe_name

    def setRecipeName(self, name):
        self.recipe_name = name

    def getAuthorName(self):
        return self.recipe_author

    def setAuthorName(self, name):
        self.recipe_author = name

    def getServings(self):
        return self.servings

    def setServings(self, serve):
        self.servings = serve

    def getIngredients(self):
        return self.ingredients

    def updateIngredients(self):
        done = False
        while not done:
            print("These are the current ingredients: ")
            for x in self.ingredients:
                print(x,":",self.ingredients[x])
        
            print("\n\nPress 1 to update existing ingredients.\nPress 2 to delete ingredients.\nPress 3 to add new ingredient.\nPress 4 to exit")
            choice = int(input())
            if choice == 1:
                print("\nEnter name of ingredient to update: ")
                ing = input()
                print("\nEnter the value:")
                val = int(input)
                self.ingredients[ing] = val

            elif choice == 2:
                print("\nEnter name of ingredient to delete: ")
                ing = input()
                del self.ingredients[ing]

            elif choice == 3:
                print("\nEnter name of ingredient to add: ")
                ing = input()
                print("\nEnter the value:")
                val = int(input())
                self.ingredients[ing] = val

            else:
                done = True
        
        self.last_updated_on = date.today()

    def getInstructions(self):
        return self.instructions

    def getItems(self):
        return self.items

    def updateInstructions(self):
        done = False
        while not done:
            print("These are the current instructions: ", self.ingredients)
        
            print("\n\nPress 1 to update existing instructions.\nPress 2 to delete instruction.\nPress 3 to add new instruction.\nPress 4 to exit")
            choice = int(input())
            if choice == 1:
                print("\nEnter index of instruction to update: ")
                ing = int(input())
                print("\nEnter the value:")
                val = input()
                self.instructions[ing] = val

            elif choice == 2:
                print("\nEnter index of instruction to delete: ")
                ing = int(input())
                del self.instructions[ing]

            elif choice == 3:
                print("\nEnter name of instruction to add: ")
                ing = input()
                print("\nEnter the index to add this:")
                val = int(input)
                self.instructions[val] = ing

            else:
                done = True

        self.last_updated_on = date.today()

    def updateItems(self):
        done = False
        while not done:
            print("These are the current items: ", self.items)
        
            print("\n\nPress 1 to delete items.\nPress 2 to add new item.\nPress 3 to exit")
            choice = int(input())
            if choice == 1:
                print("\nEnter name of item to delete: ")
                ing = input()
                self.items.remove(ing)

            elif choice == 2:
                print("\nEnter name of item to add: ")
                ing = input()
                self.items.append(ing)

            else:
                done = True

        self.last_updated_on = date.today()

    





    

    