file_name = 'alice.txt'

try:
    with open(file_name) as file_obj:
        content = file_obj.read()
except FileNotFoundError:
    print(f"Sorry, the file '{file_name}' does not exist.")
else:
    print(content)
