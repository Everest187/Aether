from leet.data import keywords
from leet.utils import encode, decode
import clipboard as pc
import re as regex

uppers = []
upperbool = False
inverted_keywords = dict((v, k) for k, v in keywords.items())

def leet_main(string):
	while True:
		if regex.compile("^[a-zA-Z ]").search(string):
			return encode(string)
		else:
			return decode(string, inverted_keywords)