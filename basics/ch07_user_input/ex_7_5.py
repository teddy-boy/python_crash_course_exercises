# Movie Ticket

prompt = "Please enter your age: "
total = 0

while True:
	age = input(prompt)
	if age == 'quit':
		break
	elif int(age) < 3:
		price = 0
		print("Your ticket is free.")
	elif int(age) < 12:
		price = 10
		print(f"Your ticket is ${price}")
		total += price
	else:
		price = 15
		print(f"Your ticket is ${price}")
		total += price
print(f"Your total price is ${total}")
