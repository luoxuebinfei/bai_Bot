#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2022/5/18 16:02
# @Author  : 落雪
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm

from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message

# 事件函数名=响应器函数("事件响应器名",[aliases={'响应关键词1','响应关键词2', }],priority=响应优先级,[rule=响应器规则])
hello = on_keyword(["你好"], priority=5)


@hello.handle()
async def hello_receive(bot: Bot, event: Event):
    await hello.finish(Message("你好啊~"))