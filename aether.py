from storage.title import Logo
from storage.sck import ScketConn
from leet.leets import leet_main
from storage.s3lf import WebsocketConn
from utils import *
from data import categories, options
import sys
from colorama import Fore

logo = Logo("e v e r e s t")
token_authed = False

def manual_auth():
	grab_token = False
	while grab_token is False:
		print(f"{Fore.LIGHTBLACK_EX}> mail:pass{Fore.RESET}", end="")
		mp = input(f"\r> ").split(":")
		token = get_token(mp[0], mp[1])
		if token[1] == 200:
			print(pn(True, 'grabbed token'));token_authed = True
			save_data("token.data", token[0])
			grab_token = True  
		else: 
			print(pn(False, 'failed to grab token')) 
			grab_token = False
	return token

if __name__ == "__main__":
	logo.clear();logo.show()
	while True:
		print(logo.watermark("root"), end="")
		opt = input(f"> ")

		if (keyvalue := options[opt]) and (categories[keyvalue] == "discord"):
			fault_token = read_data("token.data")
			try:
				token = "".join(fault_token)
			except TypeError:
				token = manual_auth()  
			else: 
				if "." in token:
					auth = auth_token(token)
					try:
						if auth[1] == 200:
							print(pn(True, 'authed token'));token_authed = True
					except TypeError:
						print(pn(False, 'failed to auth token in data'))
						token = manual_auth()
				else:
					token = manual_auth()
			user = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token}).json()
			userid = user['id'];print(info(f"Grabbed {user['username']}'s Author ID"))

		if options[opt] == "leet":
			webs = WebsocketConn(*fault_token, userid)
			webs.start_self()
