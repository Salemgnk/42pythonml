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

print_all_recipe_name()