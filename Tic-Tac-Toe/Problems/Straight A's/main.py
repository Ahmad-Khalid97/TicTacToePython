# put your python code here
grades = input()
grades = grades.split()
A_count = 0

for i in grades:
    if i == 'A':
        A_count += 1

ratio = round(A_count / len(grades), 2)
print(ratio)
