class Restaurant():
    """Create an restaurant with minimal infos"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The restaurant name is {self.name.title()}")
        print(f"It serves {self.cuisine_type.title()} food.")
    
    def open_restaurant(self):
        print(f"{self.name.title()} restaurant is now being openned.")
    
    def set_number_served(self, num_served):
        self.number_served = num_served
    
    def increment_num_served(self, incre_served):
        self.number_served += incre_served
    
    def show_number_served(self):
        print(f"We have been served {restaurant.number_served} customers.")

restaurant = Restaurant('net sai gon', 'vietnam')
# Print default value of number_served
restaurant.show_number_served()

# Modifying the value of number_served directly
restaurant.number_served = 10
restaurant.show_number_served()

# Modifying the value of number_served through a method
restaurant.set_number_served(20)
restaurant.show_number_served()

# Incrementing the value of number_served through a method
restaurant.increment_num_served(5)
restaurant.show_number_served()
