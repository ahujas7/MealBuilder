class food():
    def __init__(self, portion=0, cal=0, c=0, p=0, f=0):
        self.portionSize = portion
        self.calories = cal
        self.carbs = c
        self.protein = p
        self.fats = f
    
    def __str__(self):
         return f'Portion Size: {self.portionSize} g\nCalories: {self.calories} cal\nCarbs: {self.carbs} g\nProtein: {self.protein} g\nFats: {self.fats} g'