""" This program defines a Dish class with attributes for dish_id, dish_name, ingredients, and instructions. 
It also defines a Cookbook class to manage a collection of dishes. The Cookbook class includes methods to add a dish, 
remove a dish by its ID, display all dishes and search for dishes in the cookbook. """

# defining the class Dish with the attributes and methods
class Dish:
    def __init__(self, dish_id, dish_name, ingredients, instructions):
        self.dish_id = dish_id
        self.dish_name = dish_name

        # strip() to remove leading/trailing whitespace, capitalize() to uppercase first letter of each ingredients and instruction
        self.ingredients = [i.strip().capitalize() for i in ingredients]   
        self.instructions = [i.strip().capitalize() for i in instructions]

    def display_details(self):
        print(f"Dish ID: {self.dish_id}")
        print(f"Dish Name: {self.dish_name}")

        # join() to convert list of ingredients and instructions into a string for display
        print(f"Ingredients: {', '.join(self.ingredients)}")
        print(f"Instructions:\n{'\n'.join(self.instructions)}") 


class Cookbook:
    # initializing the Cookbook class with an empty list of dishes
    def __init__(self):
        self.dishes = []

    # method to add a dish and check for duplicates
    def add_dish(self, dish):
        for existing_dish in self.dishes:
            if existing_dish.dish_id == dish.dish_id:
                print(f"Dish ID {dish.dish_id} already exists.")
                return
        self.dishes.append(dish)
        print(f"\nDish '{dish.dish_name}' added successfully.")

    #method to remove a dish by ID
    def remove_dish(self, dish_id):
        for dish in self.dishes:
            if dish.dish_id == dish_id:
                self.dishes.remove(dish)
                print(f"\nDish with ID {dish_id} removed successfully.")
                return
        print(f"\nDish with ID {dish_id} not found in the cookbook.")

    # method to display all dishes in the cookbook
    def display_dishes(self):
        if not self.dishes:
            print("\nNo dishes in the cookbook.")
            return
        print("---------- Cookbook ----------")
        for dish in self.dishes:
            dish.display_details()
            print("-" * 15)

    # method to search for a dish by name
    def search_dish(self, dish_name):
        for dish in self.dishes:
            if dish_name.lower() in dish.dish_name.lower():
                print(f"Dish '{dish_name}' found in the cookbook:")
                dish.display_details()
                return dish
        return None

# creating an object of the Cookbook class
cookbook = Cookbook()

# menu driven interface to manage the cookbook
while True:
    print("\n----- Cookbook Menu -----")
    print("\n1. Add Dish")
    print("2. Remove Dish")
    print("3. Display Dishes")
    print("4. Search Dish")
    print("5. Exit")
    choice = input("\nEnter your choice: ")

    if choice == '1':
        dish_id = input("Enter dish ID: ")
        dish_name = input("Enter dish name: ")
        ingredients = input("Enter ingredients (comma separated): ").split(',')
        instructions = input("Enter cooking instructions (comma separated): ").split(',')

        # creating a new dish object and adding it to cookbook
        new_dish = Dish(dish_id, dish_name, ingredients, instructions)
        cookbook.add_dish(new_dish)

    elif choice == '2':
        dish_id = input("Enter dish ID to remove: ")
        cookbook.remove_dish(dish_id)

    elif choice == '3':
        cookbook.display_dishes()

    elif choice == '4':
        dish_name = input("Enter dish name to search: ")
        searchResult = cookbook.search_dish(dish_name)

        #check if the searchResult is not found
        if searchResult is None:
            print(f"\nDish '{dish_name}' not found in the cookbook.")

    elif choice == '5':
        print("\n----- Exiting the program -----")
        break

    else:
        print("Invalid choice. Please try again.")