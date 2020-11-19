text = input().split()
first_word = 0
i = 0
for word in text:
    if first_word != 0:
        text[i] = text[i].replace(word, word.capitalize())
        i += 1
    else:
        first_word += 1
        i += 1
print("".join(text))
