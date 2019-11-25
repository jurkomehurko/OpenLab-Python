def mexican_wave(word):
    result = []
    characters = list(word)

    for i, char in enumerate(characters):
        copy = characters[:]
        copy[i] = copy[i].upper()
        result.append(''.join(copy))

    return result


print(mexican_wave('hello'))
print(mexican_wave('dude'))
