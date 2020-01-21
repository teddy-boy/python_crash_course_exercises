dream_vacation = {}
name_prompt = "What's your name? "
vacation_prompt = "If you could visit one place in the world, where would you go? "

while True:
    name = input(name_prompt)
    dream_vacation[name] = input(vacation_prompt)
    another_poll = input("Do you want to take another poll (yes/no)? ")
    if another_poll == 'no':
        break

print("\n--- Poll result ---")
for name, location in dream_vacation.items():
    print(f"{name}'s dream vacation is {location}.")
