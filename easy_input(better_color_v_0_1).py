# __all__ = []

import time
from termcolor import colored
import termcolor


def in_tc_c(param):
    if not isinstance(param, str):
        return False

    return param in termcolor.COLORS


def in_tc_h(param):
    if not isinstance(param, str):
        return False

    return param in termcolor.HIGHLIGHTS


def in_tc_a(param):
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
def add_color_param(color, param):
    param_list = format_color_param(color)
    default_param_list = format_color_param(param)

    if param_list[0] == None:
        param_list[0] = default_param_list[0]

    if param_list[1] == None:
        param_list[1] = default_param_list[1]

    if param_list[2] == None:
        param_list[2] = default_param_list[2]
    elif default_param_list[2] is not None:
        for each_a in default_param_list[2]:
            if each_a not in param_list[2]:
                param_list[2].append(each_a)

    return param_list


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
            param_list[param_type] = each_param
    else:
        # 单一参数
        param_list[color_type] = color

    return param_list


# print模式对应颜色
def get_color(color="info"):
    if not color:
        return "white"
    mode_to_color_dict = {"info": "green", "warning": "yellow", "error": "red"}
    if color in mode_to_color_dict:
        return mode_to_color_dict[color]
    elif color in termcolor.COLORS:
        return color
    else:
        return "white"


# 给文字添加颜色
def color_msg(msg, color, default_color=False):
    if default_color is not False and not is_single_color_info(color):
        new_color_list = []
        for each_color in color:
            new_color_list.append(add_color_param(each_color, default_color))
        color = new_color_list

    if isinstance(msg, str):
        return color_single_msg(msg, color)
    else:
        # 判断颜色信息是否只有一条
        if is_single_color_info(color):
            return color_single_msg("".join(msg), color)

        colored_msg_list = []
        for index in range(len(msg)):
            colored_msg = color_single_msg(msg[index], color[index])
            colored_msg_list.append(colored_msg)

        return "".join(colored_msg_list)


# 给一段文字添加颜色
def color_single_msg(msg, color):
    color_param = (msg,)

    if isinstance(color, str):
        color_param += (color,)
    else:
        param_list = format_color_param(color)

        color_param += tuple(param_list)

    return colored(*color_param)


# 带时间打印
def ezprint(msg, color="info", show_time=True):
    pass


# 带格式检测的输入

# 给字符串添加时间前缀

# 获取格式化时间

# 对象是否为字符串
def is_string(val):
    return isinstance(val, str)
