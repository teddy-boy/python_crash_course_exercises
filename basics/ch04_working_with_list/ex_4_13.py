foods = ('breads', 'potato', 'noodles', 'pizza', 'pork meat')
print("Original menu:")
for element in foods:
    print(element)

print('*' * 20)

try:
    foods[2] = 'dog meat'
except:
    print("Trying to replace 'noodles' to 'dog meat'")
    print("but can not modify a tuple.")

print('*' * 20)

foods = ('apple', 'avocado', 'eggs', 'nut butter', 'chard')
print('New menu:')
for item in foods:
    print(item)
