from selfs.data import keywords

def decode(string, charset):
	for char in charset:
		string = string.replace(char, charset[char])

	return string.capitalize()

def encode(string):
	characters = []

	for chars in string.lower():
		characters.append(keywords.get(chars, chars))

	return "".join(characters)
