import os

folder = 'Nutrition Data/'

my_foods = []
count = 0

for file_name in os.listdir(folder):
    data = {'name': file_name}

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
    
    for values in data.values():
        pass    