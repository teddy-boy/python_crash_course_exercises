class Restaurant():
    """Create an restaurant with minimal infos"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant name is {self.name.title()}")
        print(f"It serves {self.cuisine_type.title()} food.")
    
    def open_restaurant(self):
        print(f"{self.name.title()} restaurant is now being openned.")

restaurant_1 = Restaurant("sea star", "vietnam")
restaurant_2 = Restaurant("oishi", 'japan')
restaurant_3 = Restaurant("Swanaka", "thai")

restaurant_1.describe_restaurant()
