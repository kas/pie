def first_non_repeated(string):
    dictionary = {}

    for character in string:
        if character not in dictionary:
            dictionary[character] = 1
        else:
            dictionary[character] += 1

    for character, count in dictionary.items():
        if count == 1:
            return character

    return None
