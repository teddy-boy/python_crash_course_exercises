prompt = "\nEnter the name of a city that you have visited."
prompt += "\n(Enter 'quit' when you finished) "

while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}")
