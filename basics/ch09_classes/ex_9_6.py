from Restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, name, food_type, flavor):
        self.flavor = flavor
        super().__init__(name, food_type)

stand = IceCreamStand('alibaba', 'ice cream', 'chocolate')
print(stand.name)
print(stand.cuisine)
print(stand.flavor)

stand.describe_restaurant()
stand.open_restaurant()
