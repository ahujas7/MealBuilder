import os
from food import Food


folder = 'Nutrition Data/'

my_foods = {}

for file_name in os.listdir(folder):
    data = {'name': file_name[:-4]}

    if os.path.isfile(os.path.join(folder, file_name)):
        current_file = open(f'{folder}{file_name}', 'r')

        for line in current_file:
            
            if line.find('Serving Size') != -1:
                data['serving'] = line
            elif line.find('Calories') != -1:
                data['cal'] = current_file.readline()
            elif line.find('Total Fat') != -1:
                data['fats'] = current_file.readline()
            elif line.find('Total Carbohydrate') != -1:
                data['carbs'] = current_file.readline()
            elif line.find('Protein') != -1:
                data['protein'] = current_file.readline()
    
    for key in data.keys():
        parts = data[key].split()
        for part in parts:
            if part[0].isdigit():
                data[key] = float(part)
    
    food = Food(data['serving'], data['cal'], data['carbs'], data['protein'], data['fats'])
    my_foods[data['name']] =  food


for name in my_foods.keys():
    my_foods[name].normalize_serving()    

max_protein = sorted(my_foods, key = lambda name: my_foods[name].protein, reverse = True)
max_carbs = sorted(my_foods, key = lambda name: my_foods[name].carbs, reverse = True)
max_fats = sorted(my_foods, key = lambda name: my_foods[name].fats, reverse = True)


breakfast = Food()

breakfast.sum_macros(my_foods['greek_yogurt'].amount(250))
breakfast.sum_macros(my_foods['ambrosia_apples'].amount(225))
breakfast.sum_macros(my_foods['bananas'].amount(125))
breakfast.sum_macros(my_foods['berry_blend'].amount(150))

lunch = Food()

lunch.sum_macros(my_foods['brown_lentils_whole'].amount(200))
lunch.sum_macros(my_foods['spinach'].amount(100))
lunch.sum_macros(my_foods['tomatoes'].amount(200)) 
lunch.sum_macros(my_foods['cucumber'].amount(150))

dinner1 = Food()

dinner1.sum_macros(my_foods['milk'].amount(400))
dinner1.sum_macros(my_foods['almonds'].amount(50))
dinner1.sum_macros(my_foods['unsalted_peanuts'].amount(40))
dinner1.sum_macros(my_foods['whole_wheat_bread'].amount(58))

dinner2 = Food()

dinner2.sum_macros(my_foods['milk'].amount(400))
dinner2.sum_macros(my_foods['almonds'].amount(50))
dinner2.sum_macros(my_foods['brown_eggs'].amount(168))
dinner2.sum_macros(my_foods['whole_wheat_bread'].amount(58))

snack1 = Food()

snack1.sum_macros(my_foods['pumpkin_seeds'].amount(70))
snack1.sum_macros(my_foods['chia_seeds'].amount(25))

snack2 = Food()

snack2.sum_macros(my_foods['pumpkin_seeds'].amount(40))
snack2.sum_macros(my_foods['flax_seeds'].amount(25))


total = Food()

total.sum_macros(breakfast)
total.sum_macros(lunch)
total.sum_macros(dinner2)
total.sum_macros(snack2)

print(total)
 