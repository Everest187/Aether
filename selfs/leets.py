from selfs.data import keywords
from selfs.utils import encode, decode
import re
from utils import info

inverted_keywords = dict((v, k) for k, v in keywords.items())


def leet_main(string):
    try:
        if re.compile("^[a-zA-Z ]").search(string):
            return encode(string)

        return decode(string, inverted_keywords)
    except TypeError:
        info("invalid chars")
