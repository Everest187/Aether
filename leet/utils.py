from leet.data import keywords


def decode(string, charset):
    for char in charset:
        string = string.replace(char, charset[char])

    return string.capitalize()


def encode(string):
    characters = []

    for chars in string.lower():
        characters.append(keywords[chars])

    return "".join(characters)
