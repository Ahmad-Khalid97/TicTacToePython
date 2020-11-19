lines_count = int(input())
name_list = []

for _ in range(lines_count):
    name_list.append(input().split())

winners = [name for [name, result] in name_list if result == 'win']

print(winners)
print(len(winners))