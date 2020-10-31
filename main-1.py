# Name: Nafisa Chowdhury
# PSID: 1591144

class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    Food_item = FoodItem()
    Food_name = input()
    Food_fat = float(input())
    Food_carbs = float(input())
    Food_protein = float(input())
    Food_item1 = FoodItem(Food_name, Food_fat, Food_carbs, Food_protein)
    num_servings = float(input())

    Food_item.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}\n".format(num_servings, Food_item.get_calories(num_servings)))
    Food_item1.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(num_servings, Food_item1.get_calories(num_servings)))
