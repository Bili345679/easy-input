from easy_input import *

# mode用来设置颜色
# 可取值["info","warning","error", "red", "green", "yellow", "blue", "magenta", "cyan", "white", False]
# 默认为 info

# 输出
ezprint("这是一段字符串")
ezprint("这是一段警告字符串", mode="warning")
ezprint("这是一段错误字符串", mode="error")
ezprint("这是一段不带时间的字符串", show_time=False)
ezprint("这是一段不带时间，调整颜色的字符串", mode="cyan", show_time=False)
print("---------")
ezprint("!@#!@#!@#", "info", show_time=False)
ezprint("!@#!@#!@#", "warning", show_time=False)
ezprint("!@#!@#!@#", "error", show_time=False)
print("---------")
ezprint("!@#!@#!@#", "red", show_time=False)
ezprint("!@#!@#!@#", "green", show_time=False)
ezprint("!@#!@#!@#", "yellow", show_time=False)
ezprint("!@#!@#!@#", "blue", show_time=False)
ezprint("!@#!@#!@#", "magenta", show_time=False)
ezprint("!@#!@#!@#", "cyan", show_time=False)
ezprint("!@#!@#!@#", "white", show_time=False)
ezprint("!@#!@#!@#", False, show_time=False)


# 输入
# 格式筛选
int_val = ezinput("输入整数", "int", default=1)
print(int_val)
float_val = ezinput("输入浮点数", "float", default=2.2)
print(float_val)
str_val = ezinput("输入字符串", "str", default="string")
print(str_val)

# 显示内容
# 不显示时间
val_1 = ezinput("input_1", show_time=False)
print(val_1)
# 不显示返回值
val_2 = ezinput("input_2", show_val=False)
print(val_2)

# 不能为空
val_3 = ezinput("input_3", not_empty_flag=True)
print(val_3)