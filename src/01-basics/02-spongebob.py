sentence = 'spongebob was the best cartoon ever, hands down'.lower()
sentence_list = []

for i, character in enumerate(sentence):
    if i % 2 == 0:
        sentence_list.append(character)
    else:
        sentence_list.append(character.upper())

print(''.join(sentence_list))