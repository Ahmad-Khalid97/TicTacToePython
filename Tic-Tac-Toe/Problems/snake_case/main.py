lowerCamelCase = input()
new_word = ''
for index in lowerCamelCase:
    if index.islower():
        new_word = new_word + index
    else:
        new_word = new_word + '_'
        new_word = new_word + index.lower()
if new_word[0] == '_':
    new_word = new_word[1:]

print(new_word)