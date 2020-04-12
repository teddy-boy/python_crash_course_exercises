file_name = 'guest_book.txt'

with open(file_name, 'a') as file_object:
    have_name = True
    while have_name:
        guest_name = input("Please enter your name: ")
        if len(guest_name) > 0:
            file_object.write(guest_name + '\n')
        else:
            have_name = False
