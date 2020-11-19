dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

sentence = input().split()
valid = 1

for word in sentence:
    if word not in dictionary:
        print(word)
        valid = 0

if valid == 1:
    print("OK")
