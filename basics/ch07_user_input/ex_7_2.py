# Restaurant Seating

promt = "How many people are you? "
people = int(input(promt))

if people > 8:
	print("You have to wait for a table")
else:
	print("Your table is ready")
