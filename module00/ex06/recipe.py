import time

cookbook = {
    "sandwich" : {
        "ingredients" : ['ham', 'bread', 'tomatoes'],
        'meal':'lunch',
        'prep_time' : 10
    },
    "cake" : {
        "ingredients" : ['flour', 'sugar', 'eggs'],
        "meal" : 'dessert',
        'prep_time' : 60
    },
    "salad" : {
        "ingredients" : ['avocado', 'arugula', 'tomatoes', 'spinach'],
        "meal" : 'lunch',
        "prep_time" : 15
    }
}

def print_all_recipe_name():
    for name in cookbook.keys():
        print(name)

def print_recipe_details():
    recipe_name = input("Please enter a recipe name to get its details: ")
    if recipe_name in cookbook:
        print(f"Recipe for {recipe_name}:")
        print("Ingredients lists :", cookbook[recipe_name].get('ingredients'))
        print("To be eaten for", cookbook[recipe_name].get('meal'))
        print(f"Take {cookbook[recipe_name].get('prep_time')} minutes of cooking")
    else:
        print("Recipe not found")

def delete_recipe():
    recipe_name = input("Please enter a recipe name to delete it: ")
    if recipe_name in cookbook:
        cookbook.pop(recipe_name)
        print(f"The recipe is succesfully deleted")
    else:
        print("Recipe not found")


def add_new_recipe():
    recipe_name = input("Please enter the name of the recipe to add: ")
    ingredients = input("Enter the list of ingredients: ").split(',')
    ingredients = [ingredient.strip() for ingredient in ingredients]
    meal = input("Please the type of meal the recipe is: ")
    try:
        prep_time = int(input("Enter the preparation time: "))
        cookbook[recipe_name] = {
            recipe_name: {
                "ingredients" : ingredients,
                "meal" : meal,
                "prep_time" : prep_time
            }
        }
        print(f"The recipe {recipe_name} has been succesfully added")
    except ValueError:
        print("The preparation time must be an integer")

def display_menu():
    print("Welcome to the Python Cookbook !")
    print("List of avaible option:")
    print("\t1: Add a recipe\n"
          "\t2: Delete a recipe\n"
          "\t3: Print a recipe\n"
          "\t4: Print the cookbook\n"
          "\t5: Quit\n")
    try:
        choice = int(input("Please select an option: "))
    except ValueError:
        print("Invalid option")
        return None
    return choice

def menu():
    while True:
        choice = display_menu()
        if choice == 1:
            add_new_recipe()
            time.sleep(1)
        elif choice == 2:
            delete_recipe()
            time.sleep(1)
        elif choice == 3:
            print_recipe_details()
            time.sleep(1)
        elif choice == 4:
            print_all_recipe_name()
            time.sleep(1)
        elif choice == 5:
            print("Bye. Exiting program !")
            break
        else :
            print("Invalid option !")
            time.sleep(2)

menu()