text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
val = int(input())
words_list = []

for wordlist in text:
    for word in wordlist:
        if len(word) <= val:
            words_list.append(word)
print(words_list)
