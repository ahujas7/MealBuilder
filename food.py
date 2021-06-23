class Food():
    def __init__(self, serving=0.0, cal=0.0, c=0.0, p=0.0, f=0.0):
        self.serving_size = round(serving, 1)
        self.calories = round(cal, 1)
        self.carbs = round(c, 1)
        self.protein = round(p, 1)
        self.fats = round(f, 1)
        
    
    def normalize_serving(self):
        self.calories = round(self.calories / self.serving_size, 3)
        self.carbs = round(self.carbs / self.serving_size, 3)
        self.protein = round(self.protein / self.serving_size, 3)
        self.fats = round(self.fats / self.serving_size, 3)

        self.serving_size = 1.000


    def macros_in_amount(self, amount):
        self.normalize_serving()
        return Food(amount, self.calories * amount, self.carbs * amount, self.protein * amount, self.fats * amount)


    def __str__(self):
         return f'Portion Size: {self.serving_size} g, Calories: {self.calories} cal, Carbs: {self.carbs} g, Protein: {self.protein} g, Fats: {self.fats} g'
         