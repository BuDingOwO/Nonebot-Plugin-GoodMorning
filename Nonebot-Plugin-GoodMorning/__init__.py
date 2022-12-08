import random

from nonebot import get_driver
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11.message import Message, MessageSegment
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.rule import Rule
from nonebot.typing import T_State
from nonebot import on_message
import asyncio
import time
import datetime

from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)

main = on_message(priority=10, block=False)


@main.handle()
async def morning_main(bot: Bot, event: Event):
    def Get_Now_Hour():
        # Now_Hour = str(time.strftime("%H", time.localtime()))
        Now_Hour = str(datetime.datetime.now().hour)
        if Now_Hour in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]:
            Now_Hour = Now_Hour[1:]
            return Now_Hour
        return Now_Hour

    # 反馈组
    Is_Morning = ['古德猫宁', '早上好!o(〃＾▽＾〃)o', '早~', '早!!!', '枣', '早上要说早上好~', f'早哦, 但现在是{Get_Now_Hour()}点诶(。・ω・。)']
    Is_Not_Morning = [f'咱不知道{Get_Now_Hour()}点算不算早上QwQ, 是不是有点晚惹UwU', f'早~，但是是{Get_Now_Hour()}点了诶qwq']
    Is_BeforeNoon = ['上午好喏~ (｡･∀･)ﾉﾞ嗨', '上午好~']
    Is_Not_BeforeNoon = [f'现在似{Get_Now_Hour()}点喏~，可能还不算上午叭xwx', '']
    Is_Noon = ['中午好~', '古德古德', '中午好哦~ 该吃饭饭了喔~', '嗷~~ 中午好！ 快到午休时间了呢，记得休息呢宝']
    Is_Not_Noon = ['现在不是中午了啦！ヽ(*。>Д<)o゜', '中午? qwq']
    Is_AfterNoon = ['下午好~', '古德啊福特奴吻']
    Is_Not_AfterNoon = ['还没到下午哇!!!o(≧口≦)o', '下午? xwx']
    Is_Evening = ['晚上好~', '古德仪唔宁~', 'w, 晚上好', f'夜间: {Get_Now_Hour()}点']
    Is_Not_Evening = ['可能现在还不是晚上捏xwx', '晚上? xwx']

    # 识别组
    Morning = ['早', '早安', '早上好', '早上坏', '早~', '早上好~', '早安~', '古德猫宁', '古德猫宁~']
    BeforeNoon = ['上午好', '上午好啊', '上午好~', '上午好啊~', '上午好呀', "上午好呀~"]
    Noon = ['午好', '中午好', '中午好~', '午好~']
    AfterNoot = ['下午好哇', '下午好~', '下午好', '下午好！']
    Evening = ['晚上好', '晚好', '晚上好！', '晚上好~']

    # 随机组
    def Is_Morning_Func():
        i = len(Is_Morning)
        res = Is_Morning[random.randint(0, len(Is_Morning) - 1)]
        return res

    def Is_Not_Morning_Func():
        i = len(Is_Not_Morning) - 1
        res = Is_Not_Morning[random.randint(0, i)]
        return res

    def Is_BeforeNoon_Func():
        i = len(Is_BeforeNoon) - 1
        res = Is_BeforeNoon[random.randint(0, i)]
        return res

    def Is_Not_BeforeNoon_Func():
        i = len(Is_Not_BeforeNoon) - 1
        res = Is_Not_BeforeNoon[random.randint(0, i)]
        return res

    def Is_Noon_Func():
        i = len(Is_Noon) - 1
        res = Is_Noon[random.randint(0, i)]
        return res

    def Is_Not_Noon_Func():
        i = len(Is_Not_Noon) - 1
        res = Is_Not_Noon[random.randint(0, i)]
        return res

    def Is_AfterNoon_Func():
        i = len(Is_AfterNoon) - 1
        res = Is_AfterNoon[random.randint(0, i)]
        return res

    def Is_Not_AfterNoon_Func():
        i = len(Is_Not_AfterNoon) - 1
        res = Is_Not_AfterNoon[random.randint(0, i)]
        return res

    def Is_Evening_Func():
        i = len(Is_Evening) - 1
        res = Is_Evening[random.randint(0, i)]
        return res

    def Is_Not_Evening_Func():
        i = len(Is_Not_Evening) - 1
        res = Is_Not_Evening[random.randint(0, i)]
        return res

    msg = str(event.get_message())
    user_id = str(event.get_user_id())
    at = MessageSegment.at(user_id)
    # hours = int(time.strftime("%H", time.localtime()))
    hours = int(datetime.datetime.now().hour)
    if hours in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        if msg in Morning:
            await main.finish(at + Is_Morning_Func())
        if msg in BeforeNoon:
            await main.finish(at + Is_Not_BeforeNoon_Func())
        if msg in Noon:
            await main.finish(at + Is_Not_Noon_Func())
        if msg in AfterNoot:
            await main.finish(at + Is_Not_AfterNoon_Func())
        if msg in Evening:
            await main.finish(at + Is_Not_Evening_Func())
        pass
    if hours in [9, 10, 11]:
        if msg in Morning:
            await main.finish(at + Is_Not_Morning_Func())
        if msg in BeforeNoon:
            await main.finish(at + Is_BeforeNoon_Func())
        if msg in Noon:
            await main.finish(at + Is_Not_Noon_Func())
        if msg in AfterNoot:
            await main.finish(at + Is_Not_AfterNoon_Func())
        if msg in Evening:
            await main.finish(at + Is_Not_Evening_Func())
        pass
    if hours in [12]:
        if msg in Morning:
            await main.finish(at + Is_Not_Morning_Func())
        if msg in BeforeNoon:
            await main.finish(at + Is_Not_BeforeNoon_Func())
        if msg in Noon:
            await main.finish(at + Is_Noon_Func())
        if msg in AfterNoot:
            await main.finish(at + Is_Not_AfterNoon_Func())
        if msg in Evening:
            await main.finish(at + Is_Not_Evening_Func())
        pass
    if hours in [13, 14, 15, 16, 17, 18, 19]:
        if msg in Morning:
            await main.finish(at + Is_Not_Morning_Func())
        if msg in BeforeNoon:
            await main.finish(at + Is_Not_BeforeNoon_Func())
        if msg in Noon:
            await main.finish(at + Is_Not_Noon_Func())
        if msg in AfterNoot:
            await main.finish(at + Is_AfterNoon_Func())
        if msg in Evening:
            await main.finish(at + Is_Not_Evening_Func())
        pass
    if hours in [20, 21, 22, 23]:
        if msg in Morning:
            await main.finish(at + Is_Not_Morning_Func())
        if msg in BeforeNoon:
            await main.finish(at + Is_Not_BeforeNoon_Func())
        if msg in Noon:
            await main.finish(at + Is_Not_Noon_Func())
        if msg in AfterNoot:
            await main.finish(at + Is_Not_AfterNoon_Func())
        if msg in Evening:
            await main.finish(at + Is_Evening_Func())
        pass
