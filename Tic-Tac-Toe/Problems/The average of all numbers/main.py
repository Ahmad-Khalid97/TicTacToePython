# put your python code here
a = int(input())
b = int(input())
result = 0
count = 0

while a <= b:
    if a % 3 == 0:
        result += a
        count += 1
    a += 1

print(result / count)