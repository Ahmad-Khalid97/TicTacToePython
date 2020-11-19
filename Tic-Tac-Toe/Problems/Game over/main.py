scores = input().split()
# put your python code here
lives = 3
count = 0

for letter in scores:
    if letter == 'C':
        count += 1
        continue
    elif letter == 'I':
        lives -= 1
        if lives == 0:
            print("Game over")
            print(count)
            break
if lives > 0:
    print("You won")
    print(count)
