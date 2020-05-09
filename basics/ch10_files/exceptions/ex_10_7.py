print("Enter two numbers, I will add them.")
print("Enter 'q' to exit.")

while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("Second number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) + int(second_num)
    except ValueError:
        print("You did not enter a number. Please try again.")
    else:
        print(f"{first_num} + {second_num} = {answer}")
