# put your python code here
num1 = float(input())
num2 = float(input())
operator = input()

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == 'pow':
    print(pow(num1, num2))
elif operator == '/' and num2 != 0:
    print(num1 / num2)
elif operator == 'mod' and num2 != 0:
    print(num1 % num2)
elif operator == 'div' and num2 != 0:
    print(num1 // num2)
else:
    print("Division by 0!")
