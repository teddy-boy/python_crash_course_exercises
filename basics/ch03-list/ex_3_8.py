locations = ['Singapore', 'Da Nang', 'Hong Kong', 'Bangkok', 'Tokyo']
print('Original list:')
print(locations)
print('*' * 10)

print('Sorted list:')
print(sorted(locations))
print('*' * 10)

print('Original list:')
print(locations)
print('*' * 10)

print('List in reverse alphabetical order:')
print(sorted(locations, reverse=True))
print('*' * 10)

print('Original list:')
print(locations)
print('*' * 10)

print("Reversed list:")
locations.reverse()
print(locations)
print('*' * 10)

print("List in original order:")
locations.reverse()
print(locations)
print('*' * 10)

print('List in alphabetical order:')
locations.sort()
print(locations)
print('*' * 10)

print('List in reverse alphabetical order:')
locations.sort(reverse=True)
print(locations)