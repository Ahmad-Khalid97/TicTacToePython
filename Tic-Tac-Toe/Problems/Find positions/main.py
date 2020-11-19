# put your python code here
number_list = [int(x) for x in input().split()]
value = int(input())

for pos, c in enumerate(number_list):
    if value not in number_list:
        print("not found")
        break
    elif c == value:
        print(pos, end=' ')
