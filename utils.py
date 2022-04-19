import json, requests
from datetime import datetime
from colorama import Fore, Style

# def op_cfg(key):
# 	with open("cfg.json", "r") as cfg_file:
# 		json_data = json.load(cfg_file)
# 		return json_data[key]

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

def save_data(filename, data):
	with open(filename, "w") as file:
		file.write(data)

def read_data(filename):
	try:
		with open(filename, "r") as file:
			return file.readlines()
	except FileNotFoundError:
		return None

def info(msg):
	return f"{Fore.MAGENTA}[{datetime.now().strftime('%S.%f')}]{Fore.RESET} {Fore.MAGENTA + Style.BRIGHT}{msg}{Fore.RESET + Style.RESET_ALL}"