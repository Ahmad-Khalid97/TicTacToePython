string_number = input()
result_list = []
i = 0

for i in range(len(string_number) - 1):
    result_list.append((int(string_number[i]) + int(string_number[i + 1])) / 2)

print(result_list)