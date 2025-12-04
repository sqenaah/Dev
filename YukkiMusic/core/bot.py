#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import sys
import asyncio

from pyrogram import Client
from pyrogram.types import BotCommand
from pyrogram.errors import BadMsgNotification

import config

from ..logging import LOGGER


class YukkiBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot")
        super().__init__(
            "YukkiMusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        # Try to start the bot with retry mechanism for time sync issues
        max_retries = 3
        for attempt in range(max_retries):
            try:
                await super().start()
                break  # Success, exit retry loop
            except BadMsgNotification as e:
                # Check if this is the time synchronization error (code 16)
                if hasattr(e, 'error_code') and e.error_code == 16:
                    LOGGER(__name__).warning(f"Time synchronization error (attempt {attempt + 1}/{max_retries}). Retrying...")
                    if attempt < max_retries - 1:
                        await asyncio.sleep(2)  # Wait before retry
                        continue
                    else:
                        LOGGER(__name__).error("Failed to start bot after multiple attempts due to time synchronization issues")
                        raise e
                elif str(e) == "[16] The msg_id is too low, the client time has to be synchronized.":
                    LOGGER(__name__).warning(f"Time synchronization error (attempt {attempt + 1}/{max_retries}). Retrying...")
                    if attempt < max_retries - 1:
                        await asyncio.sleep(2)  # Wait before retry
                        continue
                    else:
                        LOGGER(__name__).error("Failed to start bot after multiple attempts due to time synchronization issues")
                        raise e
                else:
                    raise e  # Re-raise if it's a different BadMsgNotification error

        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "Bot Started"
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
            )
            sys.exit()
        if config.SET_CMDS == str(True):
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("ping", "Check that bot is alive or dead"),
                        BotCommand("play", "Starts playing the requested song"),
                        BotCommand("skip", "Moves to the next track in queue"),
                        BotCommand("pause", "Pause the current playing song"),
                        BotCommand("resume", "Resume the paused song"),
                        BotCommand("end", "Clear the queue and leave voice chat"),
                        BotCommand("shuffle", "Randomly shuffles the queued playlist."),
                        BotCommand("playmode", "Allows you to change the default playmode for your chat"),
                        BotCommand("settings", "Open the settings of the music bot for your chat.")
                        ]
                    )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "Please promote Bot as Admin in Logger Group"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"MusicBot Started as {self.name}")
