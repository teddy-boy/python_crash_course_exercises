print("Enter 2 numbers, I'll add them.")

first_num = input("\nFirst number: ")
second_num = input("Second number: ")

try:
    answer = int(first_num) + int(second_num)
except ValueError:
    print("You did not enter a number.")
else:
    print(f"{first_num} + {second_num} = {answer}")
