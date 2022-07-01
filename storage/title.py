import fade, os, sys, importlib
from colorama import Fore, init
from data import Data
from utils import Discord, FileData
from storage.exceptions import CustomError
from utils import close


Values = Data()


class Logo:
    def __init__(self, creator):
        self.creator = creator

    @staticmethod
    def capitalize(uppercase):
        case = "".join(
            map(
                chr,
                (
                    ord(c) - (0x20 * (ord(c) in range(ord("a"), ord("z"))))
                    for c in uppercase
                ),
            )
        )
        uppercase = case
        return case

    @staticmethod
    def clear():
        os.system("@cls & @title Aether -Everest") if os.name == "nt" else os.system(
            "clear"
        )   

    @staticmethod
    def help_menu():
        print(f"""
  {Values.colors['LIGHT_GRAY']}back, b, exit: display previous window{Fore.RESET}
 """)

    def startup(self):
        default_gradient = Values.gradients["1"]
        if FileData.read_data("discord.json", "discrim") != None:
            discrim = int(FileData.read_data("discord.json", "discrim"))
            if int(discrim) % 5 > 4:
                print(default_gradient)
            elif int(discrim) % 5 in (2, 4):
                print(Values.gradients[str((int(discrim) % 5) - 1)])
            else:
                print(Values.gradients[str(int(discrim) % 5)])
        else:
            print(default_gradient)
        print(f"        [MOTD] {Values.motd['1']} [+]\n")
        print(f"{Values.colors['DARK_GRAY']}[{Values.colors['LIGHT_GRAY']}root@上の空{Values.colors['DARK_GRAY']}]{Fore.RESET}~# help")
        Logo.help_menu()
        indx = 0
        for key, value in Values.options.items():
            print(
                f"[{Fore.CYAN}{key}{Fore.RESET}] > {value['name']:<6}",
                end="" if indx % 2 == 0 else "\n",
            )
            indx += 1
        print("\n")

    def watermark(self, mark=None):
        try:
            print(
                f"{Values.colors['DARK_GRAY']}[{Values.colors['LIGHT_GRAY']}{mark}@上の空{Values.colors['DARK_GRAY']}]{Fore.RESET}~# ",
                end="",
            )
            inp = input()
            if self.capitalize(inp) in ("BACK", "B", "EXIT"):
                raise CustomError("Back To Main")

            else:
                return inp
        except EOFError:
            close(1)
