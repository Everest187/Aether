#files
from storage.title import Logo
from leet.self import WebsocketConn
from tokenF.rape import raper
from utils import *
from data import options

#internal libs
import sys

#external libs
from colorama import Fore

logo = Logo("e v e r e s t")

class Aether:
	def __init__(self):
		self.token_authed = False
		
	@staticmmethod
	def manual_auth():
		grab_token = False
		while grab_token is False:
			print(f"{Fore.LIGHTBLACK_EX}> mail:pass{Fore.RESET}", end="")
			mp = input(f"\r> ").split(":")
			token = get_token(mp[0], mp[1])
			if token[1] == 200:
				print(pn(True, 'grabbed token'));self.token_authed = True
				save_data("discord.json", token[0], "token")
				grab_token = True  
			else: 
				print(pn(False, 'failed to grab token')) 
				grab_token = False
		return token

if __name__ == "__main__":
	logo.clear()
	logo.show()
	while True:
		print(logo.watermark("root"), end="")
		opt = input(f"> ")

		if (keyvalue := options[opt]) and (keyvalue["category"] == "discord"):
			fault_token = read_data("discord.json", "token")
			try:
				token = "".join(fault_token)
			except TypeError:
				token = manual_auth()
			else: 
				if "." in token:
					auth = auth_token(token)
					try:
						if auth[1] == 200:
							print(pn(True, 'authed token'));self.token_authed = True
					except TypeError:
						print(pn(False, 'failed to auth token in data'))
						token = manual_auth()
				else:
					token = manual_auth()
			token = read_data("discord.json", "token")
			user = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token}).json()
			save_data("discord.json", user['discriminator'], "discrim")
			userid = user['id'];print(info(f"Grabbed {user['username']}'s Author ID"))
			webs = WebsocketConn(token, userid)
			if keyvalue["name"] == "1337":
				webs.leet_ed()

			elif keyvalue["name"] == "\n0\n//\n\\3-- Token\n/\\":
				raper(token)

			elif keyvalue["name"] == "Auto Response":
				webs.auto_response()
