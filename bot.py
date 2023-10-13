import nonebot
from nonebot.adapters.mirai2 import Adapter as MIRAI2Adapter



nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(MIRAI2Adapter)

nonebot.load_builtin_plugins('echo')


nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.run()