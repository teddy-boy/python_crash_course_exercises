favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ['john', 'tom', 'sarah', 'eli', 'phil']

for person in people:
    if person in favorite_languages.keys():
        print(person.title() + ", thank you for your time.")
    else:
        print(person.title() + ", please taking the poll.")
