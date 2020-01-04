players = ['charles', 'martina', 'micheal', 'florence', 'eli']

# Slice through a list
print(players[0:3])     # --> ['charles', 'martina', 'micheal']
print(players[1:4])     # --> ['martina', 'micheal', 'florence']
print(players[:4])      # --> ['charles', 'martina', 'micheal', 'florence']
print(players[2:])      # --> ['micheal', 'florence', 'eli']
print(players[-3:])     # --> ['micheal', 'florence', 'eli']

# Loop through a Slice
print('Here are the first three players from my team:')
for player in players[:3]:
    print(player.title())
