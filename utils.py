import json, requests
from datetime import datetime
from colorama import Fore, Style

def auth_token(token):
	response = requests.patch(f"https://discord.com/api/v9/users/@me/settings", headers={"Authorization": token}, json=
{"custom_status": None})
	if response.status_code == 200:
		return token, response.status_code
	else:
		return None

def get_token(mail, passw):
	token = requests.post("https://discord.com/api/v9/auth/login", json={"login": mail, "password": passw})
	return None if token.status_code != 200 else token.json()['token'], token.status_code

def pn(boolean, statement):
	return f"{Fore.LIGHTBLACK_EX}[{Fore.RESET}{Fore.MAGENTA}+{Fore.RESET}{Fore.LIGHTBLACK_EX}]{Fore.RESET} \033[0;37m{statement}{Fore.RESET}" if boolean else f"{Fore.LIGHTBLACK_EX}[{Fore.RESET}{Fore.RED}-{Fore.RESET}{Fore.LIGHTBLACK_EX}]{Fore.RESET} \033[0;37m{statement}{Fore.RESET}"

def save_data(filename, data, value):
	with open(filename, "r") as file:
		json_data = json.load(file)
		json_data[value] = data
	with open(filename, 'w') as outfile:
		json.dump(json_data, outfile)

def read_data(filename, value):
	try:
		with open(filename, "r") as file:
			json_data = json.load(file)
		return json_data[value]
	except FileNotFoundError:
		return None

def info(msg):
	return f"{Fore.MAGENTA}[{datetime.now().strftime('%S.%f')}]{Fore.RESET} {Fore.MAGENTA + Style.BRIGHT}{msg}{Fore.RESET + Style.RESET_ALL}"