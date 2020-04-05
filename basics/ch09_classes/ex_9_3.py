class User():
    def __init__(self, first_name, last_name, gender, age):
        self.full_name = first_name + " " + last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        print(f"The user's name is {self.full_name.title()}.")
        if self.gender == "male":
            print(f"He's {self.age} years old.")
        else:
            print(f"She's {self.age} years old.")
    
    def greeting_user(self):
        print(f"Hello {self.full_name.title()}, welcome to our website.")

new_user = User("lan", "hoang", "female", 34)
new_user.describe_user()
new_user.greeting_user()

print("-------------------------")

another_user = User("dzung", "nguyen", "male", 35)
another_user.describe_user()
another_user.greeting_user()
