text = input()
for letter in text:
    if not letter.isalpha():
        break
    elif letter in ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'):
        print("vowel")
    else:
        print("consonant")
