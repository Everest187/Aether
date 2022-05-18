from leet.data import keywords
from leet.utils import encode, decode
import re

inverted_keywords = dict((v, k) for k, v in keywords.items())

def leet_main(string):
	if re.compile("^[a-zA-Z ]").search(string):
		return encode(string)

	return decode(string, inverted_keywords)