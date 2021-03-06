alien_0 = {'color': 'green', 'points': 5}

print(alien_0["color"])
print(alien_0["points"])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']} now")

alien_0['speed'] = 'medium'
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be the fast alien
    x_increment = 3

# New position is old position plus increment
alien_0['x_position'] += x_increment

print("New x-position: " + str(alien_0['x_position']))

print("Original dict:")
print(alien_0)
# Remove an item (key-value pair) from a dictionary
del alien_0['points']
print("Modified dict:")
print(alien_0)
