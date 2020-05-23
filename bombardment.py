#!/user/bin/env/python3
# -*- coding:utf-8 -*-

__author__ = 'heyu<18781085152@163.com>'
__date__ = '2020/5/12'

'简易版本消息轰炸'

import time
from pynput.keyboard import Controller as key_col
from pynput.mouse import Button, Controller


# 控制键盘输入消息内容
def keyboard_input(string):
    keyboard = key_col()  # 控制键盘
    keyboard.type(string)  # 键盘输入string


# 控制鼠标点击
def mouse_click():
    mouse = Controller()  # 控制鼠标
    mouse.press(Button.left)  # 按住鼠标左键
    mouse.release(Button.left)  # 松开鼠标左键


# 主程序
def main(number, string):
    print('开始消息轰炸')
    time.sleep(5)
    for i in range(number):
        keyboard_input(string + str(i))
        mouse_click()
        time.sleep(0.3)
    print('消息轰炸结束')


if __name__ == '__main__':
    main(500, '爆炸')
