n = int(input())
my_list = []
i = 0
j = 0
for i in range(n):
    my_list.append([])
    for j in range(2):
        my_list[i].append(j + 1)
    j = 0
print(my_list)