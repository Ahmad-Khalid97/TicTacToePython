sentence = input().split()
new_words = []
for word in sentence:
    if word.endswith('s'):
        new_words.append(word)

print("_".join(new_words))
