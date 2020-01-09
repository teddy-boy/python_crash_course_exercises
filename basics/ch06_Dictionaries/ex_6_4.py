keywords = {
    'False': "boolean value --> false",
    'True': "boolean value --> true",
    'and': 'logic operator "and"',
    'for': 'used for looping',
    'python': 'the name of the language',
    }

print("This is a dicttionary:")
print(keywords)
print('\n')

for key, value in keywords.items():
    print(key + ': ' + value)
print("\n")

print("Keys in the dict is:")
for key in keywords.keys():
    print(key)
print("\n")

print("Value in the dict is:")
for value in keywords.values():
    print(value)
