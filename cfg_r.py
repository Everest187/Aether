import json

def ocfg(file):
	with open(file) as f:
		data = json.load(f)
		return data