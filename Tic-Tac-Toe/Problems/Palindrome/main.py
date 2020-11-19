word = input()
p = True
if len(word) % 2 != 0:
    print("Not palindrome")
else:
    if list(reversed(word)) == list(word):
        print("Palindrome")
    else:
        print("Not palindrome")
