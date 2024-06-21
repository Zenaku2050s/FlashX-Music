import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from FlashX-Music import LOGGER, app, userbot
from FlashX-Music.core.call import DAXX
from FlashX-Music.misc import sudo
from FlashX-Music.plugins import ALL_MODULES
from FlashX-Music.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("FlashX-Music.plugins" + all_module)
    LOGGER("FlashX-Music.plugins").info("လုပ်ဆောင်ချက်အောင်မြင်ပါသည်...")
    await userbot.start()
    await DAXX.start()
    try:
        await DAXX.stream_call("https://te.legra.ph/file/fc75fef760c29e8ccdf8b.mp4")
    except NoActiveGroupCall:
        LOGGER("FlashX-Music").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await DAXX.decorators()
    LOGGER("FlashX-Music").info(
        "ချန်နယ်ဂရုကိုဝင်ခြင်းဖြင့်ကူညီပါ..."
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("FlashX-Music").info("မြူးဇက်ဘော့အားရပ်တန့်လိုက်သည်....")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
