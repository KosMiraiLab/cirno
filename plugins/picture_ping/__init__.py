import base64

from nonebot import get_driver
from nonebot.adapters.mirai2 import MessageSegment
from nonebot.plugin import PluginMetadata
from PIL import Image
from nonebot.plugin.on import on_command
from nonebot.rule import to_me

from .config import Config

__plugin_meta = PluginMetadata(
    name="picture-hello-world",
    description="",
    usage="",
    config=Config,
)

global_config = get_driver().config
config = Config.parse_obj(global_config)

handler_set = on_command("picture_ping", rule=to_me(), block=True)


@handler_set.handle()
async def handle_hello():
    img = Image.new(mode='RGB', color=(255, 0, 0), size=(256, 256))
    b64_str = base64.b64encode(img.tobytes()).decode('utf-8')
    msg = MessageSegment.image(base64=b64_str)
    await handler_set.finish(msg)
