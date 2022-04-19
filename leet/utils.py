from leet.data import keywords

characters = []

def decode(string, charset):
	for char in charset:
		string = string.replace(char, charset[char])

	return string

def encode(string):
	for chrs in string:
		if chrs.isupper() is False:
			upperbool = False
		else:
			upperbool = True
			break

	if upperbool is False:
		for chars in string:
			try:
				characters.append(keywords[chars])
			except KeyError:
				characters.append(chars)
	else:
		for chars in string:
			if chars.isupper():
				characters.append(keywords[chars.lower()])
			else:
				characters.append(chars)
	join = "".join(characters)
	characters.clear()
	return join