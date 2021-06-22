class Food():
    def __init__(self, name=None, serving=0.0, cal=0.0, c=0.0, p=0.0, f=0.0):
        self.name = name
        self.serving_size = serving
        self.calories = cal
        self.carbs = c
        self.protein = p
        self.fats = f
        
    
    def normalize_serving(self):
        self.calories = self.calories / self.serving_size
        self.carbs = self.carbs / self.serving_size
        self.protein = self.protein / self.serving_size
        self.fats = self.fats / self.serving_size

        self.serving_size = 1.0


    def macros_in_amount(self, amount):
        self.normalize_serving()
        return Food(self.name, amount, self.calories * amount, self.carbs * amount, self.protein * amount, self.fats * amount)


    def __str__(self):
         return f'{self.name}\nPortion Size: {self.serving_size} g\nCalories: {self.calories} cal\nCarbs: {self.carbs} g\nProtein: {self.protein} g\nFats: {self.fats} g'
         

# red_kidney_beans = Food('Red Kidney Beans', 48, 160, 29, 11, 0.5)

# red_kidney_beans.normalize_serving()

# print(red_kidney_beans.macros_in_amount(300))