class User:
    def __init__(self, first_name, last_name, gender, age):
        self.full_name = first_name + " " + last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user's name is {self.full_name.title()}.")
        if self.gender == "male":
            print(f"He's {self.age} years old.")
        else:
            print(f"She's {self.age} years old.")

    def greeting_user(self):
        print(f"Hello {self.full_name.title()}, welcome to our website.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def show_login_attempts(self):
        print(f"You have been tried to login {self.login_attempts} times.")
