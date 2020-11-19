# put your python code here
number = int(input())
result = number
sum_of_squares = number**2

while result != 0:
    number = int(input())
    sum_of_squares = sum_of_squares + (number**2)
    result = result + number
print(sum_of_squares)
