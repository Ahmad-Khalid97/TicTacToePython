str_1 = input()
str_2 = input()
str_3 = input()

nested_list = []
nest_level = 0

for _ in range(3):
    if nest_level == 0:
        nested_list.append(str_1)
    elif nest_level == 1:
        nested_list.append([str_2])
    else:
        nested_list.append([[str_3]])
    nest_level += 1
print(nested_list)