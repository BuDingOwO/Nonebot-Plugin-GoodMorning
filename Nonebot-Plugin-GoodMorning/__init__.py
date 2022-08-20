from nonebot import get_driver
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11.message import Message, MessageSegment
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.rule import Rule
from nonebot.typing import T_State
from nonebot import on_message
import asyncio

from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)

main = on_message(priority=10, block=False)
@main.handle()
async def _(bot: Bot, event: MessageEvent or Event, state: T_State):
	msg = str(event.get_message())
	user_id = str(event.get_user_id())
	at = MessageSegment.at(user_id)
	if msg in ['早', '早安', '早上好', '早上坏']:
		await main.send(at + "早上好!")
