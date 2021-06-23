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

max_protein = sorted(my_foods, key = lambda name: my_foods[name].protein)

for name in max_protein:
    print(f'{my_foods[name]}, {name}')
