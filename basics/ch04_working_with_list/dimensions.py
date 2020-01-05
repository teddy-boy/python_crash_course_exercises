dimensions = (200, 50)
print(f"This is a tuple: {dimensions}")

print("Print elements in a tuple using index:")
print(dimensions[0])
print(dimensions[1])

# Tuple is immutable --> the code below doesn't work
# dimensions[1] = 250

# Loop thought a tuple
print('Print elements in a tuple using "for" loop:')
for item in dimensions:
    print(item)

# Although we can't modify a tuple, we can assign a new
# value to a variable that hold a tuple
dimensions = (400, 100)
print(f"This is a new tuple: {dimensions}")
