file_name = 'guest.txt'

with open(file_name, 'w') as file_object:
    guest_name = input('Please enter your name: ')
    file_object.write(guest_name)
