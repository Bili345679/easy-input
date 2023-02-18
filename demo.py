from easy_input import *

# mode用来设置颜色
# 可取值["info","warning","error", "red", "green", "yellow", "blue", "magenta", "cyan", "white", False]
# 默认为 info

# 输出
cprint("这是一段字符串")
cprint("这是一段警告字符串", mode="warning")
cprint("这是一段错误字符串", mode="error")
cprint("这是一段不带时间的字符串", show_time=False)
cprint("这是一段不带时间，调整颜色的字符串", mode="cyan", show_time=False)
print("---------")
cprint("!@#!@#!@#", "info", show_time=False)
cprint("!@#!@#!@#", "warning", show_time=False)
cprint("!@#!@#!@#", "error", show_time=False)
print("---------")
cprint("!@#!@#!@#", "red", show_time=False)
cprint("!@#!@#!@#", "green", show_time=False)
cprint("!@#!@#!@#", "yellow", show_time=False)
cprint("!@#!@#!@#", "blue", show_time=False)
cprint("!@#!@#!@#", "magenta", show_time=False)
cprint("!@#!@#!@#", "cyan", show_time=False)
cprint("!@#!@#!@#", "white", show_time=False)
cprint("!@#!@#!@#", False, show_time=False)


# 输入
# 格式筛选
int_val = cinput("输入整数", "int", default=1)
print(int_val)
float_val = cinput("输入浮点数", "float", default=2.2)
print(float_val)
str_val = cinput("输入字符串", "str", default="string")
print(str_val)

# 显示内容
# 不显示时间
val_1 = cinput("input_1", show_time=False)
print(val_1)
# 不显示返回值
val_2 = cinput("input_2", show_val=False)
print(val_2)

# 不能为空
val_3 = cinput("input_3", not_empty_flag=True)
print(val_3)