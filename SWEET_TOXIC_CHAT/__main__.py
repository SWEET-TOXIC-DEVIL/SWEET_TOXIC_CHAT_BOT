import asyncio
import importlib

from pyrogram import idle

from SWEET_TOXIC_CHAT import LOGGER, SWEET_TOXIC_CHAT
from SWEET_TOXIC_CHAT.modules import ALL_MODULES


async def anony_boot():
    try:
        await SWEET_TOXIC_CHAT.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("SWEET_TOXIC_CHAT.modules." + all_module)

    LOGGER.info(f"@{SWEET_TOXIC_CHAT.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping SWEET_TOXIC_CHAT Bot...")
