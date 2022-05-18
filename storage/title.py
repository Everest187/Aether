import fade, os
from colorama import Fore, init
from data import *
from utils import *

colors = {
    'DARK_GRAY': "\033[1;30m",
    'LIGHT_GRAY': "\033[0;37m"
}

class Logo:
	def __init__(self, creator):
		self.creator = creator

	def show(self):
		default_gradient = gradients["1"]
		if read_data("discord.json", "discrim") != None:
			discrim = int(read_data("discord.json", "discrim"))
			if int(discrim) % 5 > 4:
				print(default_gradient)
			elif int(discrim) % 5 in (2, 4): 
				print(gradients[str((int(discrim) % 5) - 1)])
			else: 
				print(gradients[str(int(discrim) % 5)])
		else:
			print(default_gradient)
		indx = 0
		for key, value in options.items():
		    print(f"[{Fore.CYAN}{key}{Fore.RESET}] > {value['name']:<6}",
			end="" if indx % 2 == 0 else "\n")
		    indx += 1
		print("\n")

	def watermark(self, mark=None):
		return f"{colors['DARK_GRAY']}[{colors['LIGHT_GRAY']}{mark}{colors['DARK_GRAY']}]{Fore.RESET} "

	def clear(self):
		os.system("@cls & @title Aether -Everest") if os.name == "nt" else os.system("clear")
