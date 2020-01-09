rivers = {
    'amazon': 'brazil',
    'nile': 'egypt',
    'mekong': 'vietnam',
    }

for key, value in rivers.items():
    print(key.title() + " runs through " + value.title())
print('\n')

print("The name of each river:")
for key in rivers.keys():
    print(key.title())
print('\n')

print("The name of each country:")
for value in rivers.values():
    print(value.title())
