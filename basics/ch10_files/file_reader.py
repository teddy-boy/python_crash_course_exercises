# Reading an Entire File
with open("pi_digits.txt") as file_object:
    content = file_object.read()
    print(content.rstrip())

# Reading Line by Line
file_name = "pi_digits.txt"
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a List of Lines from a File
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
