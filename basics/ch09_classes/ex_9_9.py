class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatlt formatted name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("The gas tank is filled.")

class Battery():
    """A simple attempt to represent an electric car's battery."""

    def __init__(self, baterry_size):
        self.baterry_size = baterry_size

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.baterry_size == 70:
            range = 240
        elif self.baterry_size == 85:
            range = 270
        print(f"This car can go approximately {range} miles on a full charge.")

    def describe_baterry(self):
        print(f"This car has a {self.baterry_size} kWh battery.")

    def upgrade_battery(self):
        if self.baterry_size < 85:
            self.baterry_size = 85

class Electric_Car(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery(70)

    def fill_gas_tank(self):
        """Overridding the method of parent class."""
        print("Electric cars don't have gas tank.")

my_tesla = Electric_Car('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_baterry()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_baterry()
my_tesla.battery.get_range()
