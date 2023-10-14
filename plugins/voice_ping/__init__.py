import pathlib
import tempfile
from nonebot import get_driver, on_command
from nonebot.adapters.mirai2 import MessageSegment
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me
from pydub import AudioSegment

from .config import Config

__plugin_meta = PluginMetadata(
    name="voice-hello-world",
    description="",
    usage="",
    config=Config,
)

global_config = get_driver().config
config = Config.parse_obj(global_config)

handler_set = on_command("voice_ping", rule=to_me(), block=True)


@handler_set.handle()
async def handle_hello():
    segment = AudioSegment.from_wav('./plugins/voice_ping/hello.wav')
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = pathlib.Path(tmpdir)
        out_file_path = tmpdir.joinpath('hello.amr')
        segment.set_frame_rate(8000).split_to_mono()[0].export(out_file_path, format='amr')
        msg = MessageSegment.voice(path=str(out_file_path))
    await handler_set.finish(msg)
