import time
from termcolor import colored, cprint
import termcolor

# 是否是 termcolor 文字颜色参数
def is_tc_c(param):
    if not isinstance(param, str):
        return False
    return param in termcolor.COLORS or param in ["info", "warning", "error"]


# 是否是 termcolor 背景色颜色参数
def is_tc_h(param):
    if not isinstance(param, str):
        return False
    return param in termcolor.HIGHLIGHTS


# 是否是 termcolor 额外参数
def is_tc_a(param):
    if not isinstance(param, list):
        return False
    for each in param:
        if not isinstance(each, str):
            return False
        if each not in termcolor.ATTRIBUTES:
            return False
    return True


# 是否是 termcolor 参数
def is_tc_p(param):
    if is_tc_c(param):
        return 0
    elif is_tc_h(param):
        return 1
    elif is_tc_a(param):
        return 2
    return False


# print模式对应颜色
def mode_to_color(mode):
    mode_to_color_dict = {"info": "green", "warning": "yellow", "error": "red"}
    if mode in mode_to_color_dict:
        return mode_to_color_dict[mode]
    else:
        return mode


# 是否是单条颜色信息
def is_single_color(color):
    if isinstance(color, str):
        if is_tc_p(color) is not False:
            return True
        else:
            raise "color 参数非 termcolor 可选参数"

    if not isinstance(color, list):
        raise "color 参数仅为 str 型或 list 型"

    if is_tc_a(color):
        return True

    param_count_list = [0, 0, 0]
    for each_param in color:
        param_type = is_tc_p(each_param)
        # 参数不是 termcolor 的参数，可能是 color 列表
        if param_type is False:
            return False
        else:
            param_count_list[param_type] += 1
        if 2 in param_count_list:
            return False
    return True


# 格式化颜色参数(参数仅为单条数据)
def format_color(param):
    param_list = [None, None, None]
    param_type = is_tc_p(param)
    if param_type is False:
        # 参数列表
        for each_param in param:
            # 颜色类型
            param_type = is_tc_p(each_param)
            # 未知类型
            if param_type is False:
                continue
            if param_type == 0:
                each_param = mode_to_color(each_param)
            param_list[param_type] = each_param
    else:
        # 单一参数
        if param_type == 0:
            param = mode_to_color(param)
        param_list[param_type] = param

    return param_list


# 添加默认颜色
def add_def_color(color, def_color):
    if color[0] is None and def_color[0] is not None:
        color[0] = def_color[0]
    if color[1] is None and def_color[1] is not None:
        color[1] = def_color[1]

    if color[2] is None and def_color[2] is not None:
        color[2] = def_color[2]
    elif def_color[2] is not None:
        for each_def_color_p in def_color[2]:
            if each_def_color_p not in color[2]:
                color[2].append(each_def_color_p)
    return color


def color_str(string, color, def_color=False):
    # color
    if is_single_color(color):
        color_list = [format_color(color)]
    else:
        color_list = []
        for each_color in color:
            if not is_single_color(each_color):
                raise "颜色格式错误"
            color_list.append(format_color(each_color))

    # def_color
    if def_color is not False:
        if is_single_color(def_color):
            def_color = format_color(def_color)
        else:
            def_color = format_color(def_color[0])

        defed_color_list = []
        for each_color in color_list:
            defed_color_list.append(add_def_color(each_color, def_color))
        color_list = defed_color_list
    # str
    if isinstance(string, str):
        return color_single_str(string, color_list[0])

    if not isinstance(string, list):
        raise "string 参数仅为 str 型或 list 型"

    colored_str_list = []
    for index in range(len(string)):
        if not isinstance(string[index], str):
            raise "string 参数格式错误"

        this_color = (
            color_list[index]
            if index < len(color_list)
            else (def_color if def_color is not False else [None, None, None])
        )

        colored_str_list.append(color_single_str(string[index], this_color))

    return "".join(colored_str_list)


# 给一段文字添加颜色
def color_single_str(string, color):
    color_param = (string,)

    color_param += tuple(color)

    return colored(*color_param)


# ezprint
#   msg 信息
#       str
#       list
#   color 颜色参数
#       color
#           list
#               lsit[list]
#   show_time 显示时间
#   def 默认颜色参数
#       color
#           list
#               lsit[list]


def ezprint(msg, color="info", show_time=True, def_color=False, end=None):
    if isinstance(msg, str):
        msg = [msg]
    elif not isinstance(msg, list):
        raise "ezinput msg 参数 仅为 str 型或 list 型"

    if show_time:
        msg = [get_date_str() + "\t"] + msg

    print(color_str(msg, color, def_color))


# 获取格式化时间
def get_date_str(timestamp=False):
    if not timestamp:
        timestamp = time.time()
    timestamp = time.localtime(timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", timestamp)
