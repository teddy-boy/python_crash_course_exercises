favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# Looping through both keys and values in a dict
for name, language in favorite_languages.items():
    print("\n")
    print(name.title() + "'s favorite language is " +
        language.title())

# Looping through keys via keys() method
for name in favorite_languages.keys():
    print(name)
print("\n")

# Looping through keys via normal "for loop"
for name in favorite_languages:
    print(name)
print("\n")

# Looping through value in a dictionary
for value in favorite_languages.values():
    print(value.title())
print("\n")
