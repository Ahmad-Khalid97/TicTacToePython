number_list = []
number = input()
while number != '.':
    number_list.append(float(number))
    number = input()
print(min(number_list))
