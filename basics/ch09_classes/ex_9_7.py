from User import User

class Admin(User):

    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = ["add post", "delete post", "ban users"]

    def show_privileges(self):
        print("ou can:")
        for privilege in self.privileges:
            print(privilege.title())

admin = Admin("dzung", "nguyen", "male", 35)
admin.describe_user()
admin.greeting_user()
admin.show_privileges()
