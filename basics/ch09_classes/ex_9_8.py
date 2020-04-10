from User import User

class Privileges:

    def __init__(self):
        self.privileges = ["add post", "delete post", "ban users"]

    def show_privileges(self):
        print("You can:")
        for privilege in self.privileges:
            print(privilege.title())

class Admin(User):
    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = Privileges()

admin = Admin("lan", "hoang", 'female', 34)
admin.describe_user()
admin.greeting_user()
admin.privileges.show_privileges()
