import nonebot
from nonebot.adapters.mirai2 import Adapter as MIRAI2Adapter
from nonebot.adapters.console import Adapter as ConcoleAdapter
import typer


def main(console_only: bool = False):
    nonebot.init()
    driver = nonebot.get_driver()

    adaptor = ConcoleAdapter if console_only else MIRAI2Adapter
    if console_only:
        driver.register_adapter(ConcoleAdapter)
    else:
        driver.register_adapter(MIRAI2Adapter)

    nonebot.load_builtin_plugins("echo")
    nonebot.load_from_toml("pyproject.toml")

    nonebot.run()


if __name__ == "__main__":
    typer.run(main)
