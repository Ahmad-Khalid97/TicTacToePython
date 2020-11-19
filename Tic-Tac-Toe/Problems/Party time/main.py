c = True
name_list = []
while c:
    name = input()
    if name == '.':
        c = False
    else:
        name_list.append(name)
print(name_list)
print(len(name_list))
