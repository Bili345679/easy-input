from easy_input import *
from termcolor import cprint

ezprint("hello,world", ["underline"])
ezprint("hello,world", "red")
ezprint("hello,world", "info")
ezprint(["hello,world", "hello,python"], ["red", "blue"])
ezprint(["hello,world", "hello,python"], ["red", ["blue", ["bold"]]])
ezprint(
    ["hello,world", "hello,python"],
    ["red", ["blue", ["bold"]]],
    def_color=["underline"],
)
ezprint(
    ["hello,world", "hello,python"],
    ["red", ["blue", ["bold"]]],
    def_color=[["underline"]],
)
ezprint(
    ["hello,world", "hello,python"],
    ["red", ["blue", ["bold"]]],
    def_color=["on_green", ["underline"]],
)
ezprint(
    ["hello,world", "hello,python"],
    ["red", ["blue", ["bold"]]],
    def_color=["on_green"],
)

ezprint(
    ["hello,world", "hello,python"],
    ["red", ["blue", ["bold"]]],
    def_color="on_green",
)
ezprint("Hello,World!")
ezprint("Hello,World!", "warning")
ezprint("Hello,World!", "error")
ezprint("Hello,World!", "error", show_time=False)
ezprint("Hello,World!", def_color=[["underline"]])
ezprint("Hello,World!", def_color=[["underline"]], end="")
ezprint("Hello,World!", def_color=[["underline"]], end="")
