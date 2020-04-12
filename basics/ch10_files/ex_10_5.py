file_name = 'programming_poll.txt'

with open(file_name, 'a') as file_object:
    have_reason = True
    file_object.write("The reasons people love programming are:\n")
    while have_reason:
        reason = input("Why do you love programming: ")
        if len(reason) > 0:
            file_object.write(reason + '\n')
        else:
            have_reason = False