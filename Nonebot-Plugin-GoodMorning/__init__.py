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
async def morning_main(bot: Bot, event: MessageEvent or Event, state: T_State):
    def Get_Now_Hour():
        # Now_Hour = str(time.strftime("%H", time.localtime()))
        Now_Hour = str(datetime.datetime.now().hour)
        if Now_Hour in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]:
            Now_Hour = Now_Hour[1:]
            return Now_Hour
        return Now_Hour

    # 反馈组
    Is_Morning = "早上好!o(〃＾▽＾〃)o"
    Is_Not_Morning = "咱不知道" + Get_Now_Hour() + "点算不算早上QwQ, 是不是有点晚惹UwU"
    Is_BeforeNoon = "上午好喏~ (｡･∀･)ﾉﾞ嗨"
    Is_Not_BeforeNoon = "现在似" + Get_Now_Hour() + "点喏~，可能还不算上午叭xwx"
    Is_Noon = "中午好~"
    Is_Not_Noon = "现在不是中午了啦！ヽ(*。>Д<)o゜"
    Is_AfterNoon = "下午好~"
    Is_Not_AfterNoon = "还没到下午哇!!!o(≧口≦)o"
    Is_Evening = "晚上好~"
    Is_Not_Evening = "可能现在还不是晚上捏xwx"

    # 识别组
    Morning = ['早', '早安', '早上好', '早上坏', '早~', '早上好~', '早安~']
    BeforeNoon = ['上午好', '上午好啊', '上午好~', '上午好啊~', '上午好呀', "上午好呀~"]
    Noon = ['午好', '中午好', '中午好~', '午好~']
    AfterNoot = ['下午好哇', '下午好~', '下午好', '下午好！']
    Evening = ['晚上好', '晚好', '晚上好！', '晚上好~']

    msg = str(event.get_message())
    user_id = str(event.get_user_id())
    at = MessageSegment.at(user_id)
    # hours = int(time.strftime("%H", time.localtime()))
    hours = int(datetime.datetime.now().hour)
    if hours in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        if msg in Morning:
            await main.finish(at + Is_Morning)
        if msg in BeforeNoon:
            await main.finish(at + Is_Not_BeforeNoon)
        if msg in Noon:
            await main.finish(at + Is_Not_Noon)
        if msg in AfterNoot:
            await main.finish(at + Is_Not_AfterNoon)
        if msg in Evening:
            await main.finish(at + Is_Not_Evening)
        pass
    if hours in [9, 10, 11]:
        if msg in Morning:
            await main.finish(at + Is_Not_Morning)
        if msg in BeforeNoon:
            await main.finish(at + Is_BeforeNoon)
        if msg in Noon:
            await main.finish(at + Is_Not_Noon)
        if msg in AfterNoot:
            await main.finish(at + Is_Not_AfterNoon)
        if msg in Evening:
            await main.finish(at + Is_Not_Evening)
        pass
    if hours in [12]:
        if msg in Morning:
            await main.finish(at + Is_Not_Morning)
        if msg in BeforeNoon:
            await main.finish(at + Is_Not_BeforeNoon)
        if msg in Noon:
            await main.finish(at + Is_Noon)
        if msg in AfterNoot:
            await main.finish(at + Is_Not_AfterNoon)
        if msg in Evening:
            await main.finish(at + Is_Not_Evening)
        pass
    if hours in [13, 14, 15, 16, 17, 18, 19]:
        if msg in Morning:
            await main.finish(at + Is_Not_Morning)
        if msg in BeforeNoon:
            await main.finish(at + Is_Not_BeforeNoon)
        if msg in Noon:
            await main.finish(at + Is_Not_Noon)
        if msg in AfterNoot:
            await main.finish(at + Is_AfterNoon)
        if msg in Evening:
            await main.finish(at + Is_Not_Evening)
        pass
    if hours in [20, 21, 22, 23]:
        if msg in Morning:
            await main.finish(at + Is_Not_Morning)
        if msg in BeforeNoon:
            await main.finish(at + Is_Not_BeforeNoon)
        if msg in Noon:
            await main.finish(at + Is_Not_Noon)
        if msg in AfterNoot:
            await main.finish(at + Is_Not_AfterNoon)
        if msg in Evening:
            await main.finish(at + Is_Evening)
        pass
