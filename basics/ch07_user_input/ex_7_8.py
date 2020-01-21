sandwich_orders = ['tuna', 'beef', 'pork']
finished_sandwich = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwich.append(sandwich)

print("Here are finished sandwichs:")
for sandwich in finished_sandwich:
    print(sandwich.title())
