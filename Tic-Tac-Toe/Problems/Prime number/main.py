number = int(input())
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("This number is not prime")
            break
        elif number % i != 0 and i + 1 == number:
            print("This number is prime")
        else:
            continue
else:
    print("This number is not prime")
