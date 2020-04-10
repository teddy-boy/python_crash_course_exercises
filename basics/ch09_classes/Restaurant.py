class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.name.title()}.")
        print(f"It serves {self.cuisine.title()}.")

    def open_restaurant(self):
        print(f"{self.name.title()} restaurant is now being openned.")
