import fade, os
from colorama import Fore, init


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
	1 > 1337 .    ▪ 	     ▪   
	2 > A Token's Death Lullaby •   	.     
	       ·              ▪          •          •
	└──────────────────────────────────────────────────┘
			"""))

	def watermark(self, mark=None):
		return f"{colors['DARK_GRAY']}[{colors['LIGHT_GRAY']}{mark}{colors['DARK_GRAY']}]{Fore.RESET} "

	def clear(self):
		os.system("@cls & @title Teach Me How To Cry .") if os.name == "nt" else os.system("clear")