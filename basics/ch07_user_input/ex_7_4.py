# Pizza Topping

prompt = "Please enter the topping that you want: "
prompt += "\n(Enter 'quit' when you finished) "

while True:
	topping = input(prompt)
	if topping == 'quit':
		break
	else:
		print(f"\nI'll add {topping} to the pizza.\n")
