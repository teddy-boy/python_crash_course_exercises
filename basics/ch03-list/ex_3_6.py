guest_list = ['Lan', 'Chuc', 'Minh']

print('Hi ' + guest_list[0] + ', please come to have dinner with me')
print('Hi ' + guest_list[1] + ', please come to have dinner with me')
print('Hi ' + guest_list[2] + ', please come to have dinner with me')
print('*' * 10)

print('Oop! ' + guest_list[2] + ' can\'t make it today.')
guest_list[2] = 'Ngoc'
print('Hi ' + guest_list[2] + ', please come to have dinner with me')
print('*' * 10)

print("Oh, I found a bigger dinner table. Let's invite more people.")
guest_list.insert(0, 'Trang')
guest_list.insert(2, 'Linh')
guest_list.append('Quynh')
print('Hi ' + guest_list[0] + ', please come to have dinner with me')
print('Hi ' + guest_list[2] + ', please come to have dinner with me')
print('Hi ' + guest_list[-1] + ', please come to have dinner with me')