def read_file(file_name):
    try:
        with open(file_name) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        pass
    else:
        for line in lines:
            print(line.rstrip().title())

read_file('dog.txt')
read_file('cats.txt')
