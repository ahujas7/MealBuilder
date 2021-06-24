class Food():
    def __init__(self, serving=0.0, cal=0.0, c=0.0, p=0.0, f=0.0):
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

        self.serving_size = 1.000


    def amount(self, amount):
        self.normalize_serving()
        return Food(amount, self.calories * amount, self.carbs * amount, self.protein * amount, self.fats * amount)
    
    def sum_macros(self, food):
        self.serving_size += food.serving_size
        self.calories += food.calories
        self.carbs += food.carbs
        self.protein += food.protein
        self.fats += food.fats



    def __str__(self):
         return f'Portion Size: {round(self.serving_size, 1)} g, Calories: {round(self.calories, 1)} cal, Carbs: {round(self.carbs, 1)} g, Protein: {round(self.protein, 1)} g, Fats: {round(self.fats, 1)} g'
         