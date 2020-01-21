sandwich_orders = ['tuna', 'pastrami', 'beef', 'pastrami', 'pork', 'pastrami']
finished_sandwich = []

print("The restaurant has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwich.append(sandwich)

print("Here are finished sandwichs:")
for sandwich in finished_sandwich:
    print(sandwich.title())
