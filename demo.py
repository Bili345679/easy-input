from easy_input import *
from termcolor import cprint

print(color_str("hello,world", ["underline"]))
print(color_str("hello,world", "red"))
print(color_str("hello,world", "info"))
print(color_str(["hello,world", "hello,python"], ["red", "blue"]))
print(color_str(["hello,world", "hello,python"], ["red", ["blue", ["bold"]]]))
print(
    color_str(
        ["hello,world", "hello,python"],
        ["red", ["blue", ["bold"]]],
        ["underline"],
    )
)
print(
    color_str(
        ["hello,world", "hello,python"],
        ["red", ["blue", ["bold"]]],
        [["underline"]],
    )
)
print(
    color_str(
        ["hello,world", "hello,python"],
        ["red", ["blue", ["bold"]]],
        ["on_green", ["underline"]],
    )
)
print(
    color_str(
        ["hello,world", "hello,python"],
        ["red", ["blue", ["bold"]]],
        ["on_green"],
    )
)
print(
    color_str(
        ["hello,world", "hello,python"],
        ["red", ["blue", ["bold"]]],
        "on_green",
    )
)

ezprint("Hello,World!")
ezprint("Hello,World!", "warning")
ezprint("Hello,World!", "error")
ezprint("Hello,World!", "error", show_time=False)
ezprint("Hello,World!", def_color=[["underline"]])
