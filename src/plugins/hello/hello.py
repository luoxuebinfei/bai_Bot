#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2022/5/18 15:50
# @Author  : 落雪
# @Site    : 
# @File    : hello.py
# @Software: PyCharm

# 事件响应器函数
from nonebot import on_command, on_startswith
# rule事件响应规则（需要@bot才能响应事件）
from nonebot.rule import to_me
# bot使用的对象和字典
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

from nonebot.adapters.onebot.v11 import (
    Bot,
    GroupMessageEvent,
    Message,
    MessageEvent,
)
# 使用无头浏览器访问api地址
import urllib3
# 处理api返回的json数据
import json

# 事件函数名=响应器函数("事件响应器名",[aliases={'响应关键词1','响应关键词2', }],priority=响应优先级,[rule=响应器规则])
hello = on_command("hello", aliases={'你好/Hi/hi', }, priority=5)


@hello.handle()
async def hello_receive(bot: Bot, event: Event, state: T_State):
    await hello.send(Message("你好啊~"))
