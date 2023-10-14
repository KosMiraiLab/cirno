from nonebot import get_driver
from nonebot.adapters.mirai2 import MessageSegment
from nonebot.plugin import PluginMetadata
from nonebot.plugin.on import on_command
from nonebot.rule import to_me

from .config import Config

__plugin_meta = PluginMetadata(
    name="hello-world",
    description="",
    usage="",
    config=Config,
)

global_config = get_driver().config
config = Config.parse_obj(global_config)

handler_set = on_command("ping", rule=to_me(), block=True)


@handler_set.handle()
async def handle_hello():
    await handler_set.finish("pong")
