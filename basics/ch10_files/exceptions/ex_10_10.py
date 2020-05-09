file_name = 'the_importance_of_being_earniest.txt'

with open(file_name) as file_object:
    contents = file_object.read()
    word = input("Enter the word that you want to count: ")
    print(contents.lower().count(word))