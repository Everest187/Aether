#files
from storage.title import Logo
from storage.exec import execs
from utils import Discord, FileData, pn, info, close
from data import Data
from storage.exceptions import CustomError

#internal libs
import sys

#external libs
from colorama import Fore

logo = Logo("e v e r e s t")

class Aether:
	def __init__(self):
		self.token_authed = False

	def manual_auth(self):
		grab_token = False
		while grab_token is False:
			print(f"{Fore.LIGHTBLACK_EX}> mail:pass{Fore.RESET}", end="")
			mp = input(f"\r> ").split(":")
			token = Discord.get_token(mp[0], mp[1])
			if token[1] == 200:
				pn(True, 'grabbed token');self.token_authed = True
				FileData.save_data("./db/discord.json", token[0], "token")
				grab_token = True  
			else: 
				pn(False, 'failed to grab token')
				grab_token = False
		return token

	def main(self):
		try:
			opt = logo.watermark("root")

			if (keyvalue := Data.options[opt]) and (keyvalue["category"] == "discord"):
				fault_token = FileData.read_data("./db/discord.json", "token")
				try:
					token = "".join(fault_token)
				except TypeError:
					token = self.manual_auth()
				else: 
					if "." in token:
						auth = Discord.auth_token(token)
						try:
							if auth[1] == 200:
								pn(True, 'authed token');self.token_authed = True
						except TypeError:
							pn(False, 'failed to auth token in data')
							token = self.manual_auth()
					else:
						token = self.manual_auth()
				token = FileData.read_data("./db/discord.json", "token")
				user = Discord.discord_data(token)
				FileData.save_data("./db/discord.json", user['discriminator'], "discrim")
				info(f"Grabbed {user['username']}'s Author ID")
				execs(keyvalue, token, user['id'])
		except CustomError:
			return
		except KeyboardInterrupt:
			close(1)

if __name__ == "__main__":
	aether = Aether()
	while True:
		Logo.clear()
		logo.startup()
		aether.main() 