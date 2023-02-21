import sys

from termcolor import colored, cprint
import termcolor

print(termcolor.COLORS)
print(termcolor.HIGHLIGHTS)
print(termcolor.ATTRIBUTES)

cprint("Hello, World!", "green")
cprint("Hello, World!", "yellow")
cprint("Hello, World!", "blue")
cprint("Hello, World!", "magenta")
cprint("Hello, World!", "cyan")
cprint("Hello, World!", "white")

cprint("Hello, World!", "red", ["on_bold"])
