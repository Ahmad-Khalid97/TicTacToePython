string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
index = 0
vowelcount = 0

for index in string:
    if index in vowels:
        vowelcount = vowelcount + 1
print(vowelcount)
