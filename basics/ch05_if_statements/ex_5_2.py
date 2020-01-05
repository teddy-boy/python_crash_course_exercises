my_car = ['Honda', 175]
friend_car = ['Mercedes', 250]
luxury_cars = ['bmw', 'mercedes', 'ferrari', 'porsche']
standard_hp = 200

print("Is my car a luxury car?")
print(my_car[0] in luxury_cars)

print("Is my friend's car a luxury car?")
print(friend_car[0].lower() in luxury_cars)

print("Is my car a high performance car?")
print(my_car[1] > standard_hp)

print("Is my friend's car a high performance car?")
print(friend_car[1] > standard_hp)

print("So my car is just a normal car, right?")
print(my_car[0].lower() not in luxury_cars and my_car[1] <= standard_hp)
