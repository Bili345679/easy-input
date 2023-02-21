# __all__ = []

import time
from termcolor import colored
import termcolor


def in_tc_c(param):
    info_type_list = ["info", "warning", "error"]
    if not isinstance(param, str):
        return False

    return (param in termcolor.COLORS) or (param in info_type_list)


def in_tc_h(param):
    if not isinstance(param, str):
        return False

    return param in termcolor.HIGHLIGHTS


def in_tc_a(param):
    print(param)
    if not isinstance(param, list):
        return False
    for each_param in param:
        if each_param not in termcolor.ATTRIBUTES:
            return False
    return True


# 颜色参数类型
def in_tc_p(param):
    if in_tc_c(param):
        return 0
    elif in_tc_h(param):
        return 1
    elif in_tc_a(param):
        return 2
    return False


# 是否只是一条颜色信息
def is_single_color_info(param):
    if isinstance(param, str):
        return True

    if len(param):
        return False

    param_type_list = [0, 0, 0]
    for each_param in param_type_list:
        if in_tc_c(each_param):
            param_type_list[0] += 1
        elif in_tc_h(each_param):
            param_type_list[1] += 1
        elif in_tc_h(each_param):
            param_type_list[2] += 1
        else:
            return False
        if 2 in param_type_list:
            return False

    return True


# 给颜色信息添加颜色参数
def add_color_param(color, default_color):

    if color[0] == None:
        color[0] = default_color[0]

    if color[1] == None:
        color[1] = default_color[1]

    if color[2] == None:
        color[2] = default_color[2]
    elif default_color[2] is not None:
        for each_a in default_color[2]:
            if each_a not in color[2]:
                color[2].append(each_a)

    return color


# 格式化参数类型
def format_color_param(color):
    param_list = [None, None, None]
    color_type = in_tc_p(color)
    if color_type is False:
        # 参数列表
        for each_param in color:
            # 颜色类型
            param_type = in_tc_p(each_param)
            # 未知类型
            if param_type is False:
                continue
            if param_type == 0:
                each_param = get_color(each_param)
            param_list[param_type] = each_param
    else:
        # 单一参数
        if color_type == 0:
            color = get_color(color)
        param_list[color_type] = color

    return param_list


# print模式对应颜色
def get_color(color):
    mode_to_color_dict = {"info": "green", "warning": "yellow", "error": "red"}
    if color in mode_to_color_dict:
        return mode_to_color_dict[color]
    else:
        return color


# 给文字添加颜色
def color_msg(msg, color, default_color=False):
    print("#####################")
    print(msg)
    print(color)
    print(default_color)
    # 格式化颜色并转换成列表
    if is_single_color_info(color):
        color = [format_color_param(color)]
    else:
        new_color_list = []
        for each_color in color:
            new_color_list.append(format_color_param(each_color))
        color = new_color_list

    # 默认颜色
    if default_color is not False:
        print("asd")
        default_color = format_color_param(default_color)
        print("asd")
        new_color_list = []
        for index in range(len(msg)):
            print(color[index], "140")
            if index >= len(color):
                new_color_list.append(default_color)
            else:
                new_color_list.append(add_color_param(color[index], default_color))
        color = new_color_list
    print(color)

    # 单独一条msg
    if isinstance(msg, str):
        return color_single_msg(msg, format_color_param(color[0]))

    # 多条msg
    colored_msg_list = []

    for index in range(len(msg)):
        if index >= len(color):
            colored_msg_list.append(msg[index])
            continue

        colored_msg_list.append(color_single_msg(msg[index], color[index]))

    return "".join(colored_msg_list)


# 给一段文字添加颜色
def color_single_msg(msg, color):
    color_param = (msg,)
    color_param += tuple(color)
    return colored(*color_param)


# 带时间打印
def ezprint(msg, color="info", show_time=True, default_color=False):
    if show_time:
        date_str = "[" + get_date_str() + "]\t"
        if is_single_color_info(color):
            msg = color_msg(date_str, color) + msg
        else:
            if isinstance(msg, str):
                msg = [date_str, msg]
            else:
                msg = [date_str] + msg
    print(color_msg(msg, color, default_color))


# 带格式检测的输入

# 给字符串添加时间前缀

# 获取格式化时间
def get_date_str(timestamp=False):
    if not timestamp:
        timestamp = time.time()
    timestamp = time.localtime(timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", timestamp)


# 对象是否为字符串
def is_string(val):
    return isinstance(val, str)
