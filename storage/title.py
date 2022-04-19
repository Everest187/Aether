import fade, os
from colorama import Fore, init
from data import options


colors = {
    'DARK_GRAY': "\033[1;30m",
    'LIGHT_GRAY': "\033[0;37m"
}

def purplepink(text):
    os.system(""); faded = ""
    red = 40
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

class Logo:
	def __init__(self, creator):
		self.creator = creator

	def show(self):
		print(purplepink(f"""
	┌──────────────────────────────────────────────────┐	 
		•▄▄▄· ▄▄▄ .▄▄▄▄▄ ▄ .▄▄▄▄ .▄▄▄  	▪
	  ·	▐█ ▀█ ▀▄.▀·•██  ██▪▐█▀▄.▀·▀▄ █·	 
		▄█▀▀█ ▐▀▀▪▄ ▐█.▪██▀▐█▐▀▀▪▄▐▀▀▄ 	▪	•
	 ·	▐█ ▪▐▌▐█▄▄▌ ▐█▌·██▌▐▀▐█▄▄▌▐█•█▌	
		 ▀  ▀  ▀▀▀  ▀▀▀ ▀▀▀ · ▀▀▀ .▀  ▀ 
	   •		  •	{self.creator}	·	  ▪               
  		·	▪		·					
	•		  ·		     ·		▪     
		 .    ▪ 	     ▪   
				 •   	.     
	       ·              ▪          •          •
	└──────────────────────────────────────────────────┘
			"""))
		indx = 0
		for key, value in options.items():
		    print(f"[{Fore.MAGENTA}{key}{Fore.RESET}] > {value['name']:<10}",
			end="" if indx % 2 == 0 else "\n");print()
		    indx += 1

	def watermark(self, mark=None):
		return f"{colors['DARK_GRAY']}[{colors['LIGHT_GRAY']}{mark}{colors['DARK_GRAY']}]{Fore.RESET} "

	def clear(self):
		os.system("@cls & @title Teach Me How To Cry .") if os.name == "nt" else os.system("clear")
