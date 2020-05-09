def count_words(file_name):
    """Count the approximate number of words in a file."""
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print(f"Sorry, the file '{file_name}' does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file '{file_name}' has about {num_words} words.")

file_name = 'alice.txt'
count_words(file_name)
