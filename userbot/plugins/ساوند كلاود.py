#๐๐๐๐๐๐ค๐ฃ ยฎ
# Port to UserBot
# modified by @ZedThon
# Copyright (C) 2022.

import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import *

@zedthon.on(zelzal_cmd(pattern="ุณุงููุฏ$", outgoing=True))
@zedthon.on(sudo_cmd(pattern="ุณุงููุฏ$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**```ุจุงููุฑุฏ ุนูู ุงูุฑุงุจูุท ุญูุจูู ๐งธ๐```**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**```ุจุงููุฑุฏ ุนูู ุงูุฑุงุจูุท ุญูุจูู ๐งธ๐```**")
        return
    chat = "@DeezerMusicBot"
    catevent = await edit_or_reply(event, "**โฎ โ ุฌูุงุฑู ุงูุชุญูููู ูู ุณูุงููุฏ ูููุงูุฏ ุงูุชุธูุฑ ููููุงู  โฌโญ... ๐ซโฐ**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=595898211)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**โโุชุญููู ูู ุงููู ูู ุชููู ุจุญุธูุฑ ุงูุจูุช @downloader_tiktok_bot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**๐คจ๐...ุ**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@borg.on(zelzal_cmd(pattern="ูููุฏ ?(.*)"))
async def zed(event):
    if event.fwd_from:
        return
    zedr = event.pattern_match.group(1)
    zelzal = "@DeezerMusicBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(zelzal, zedr)
    await tap[0].click(event.chat_id)
    await event.delete()


CMD_HELP.update(
    {
        "ุณุงููุฏ ููุงูุฏ": "**ุงุณู ุงูุงุถุงููู : **`ุณุงููุฏ ููุงูุฏ`\
    \n\n**โฎโขโ ุงูุงููุฑ โฆ **`.ูููุฏ` + ุงุณูู ุงูุงุบูููู\
    \n**ุงูุดูุฑุญ โขโข **ุจุญุซ ูุชุญููู ุงูุงุบูุงูู ูู ุณูุงููุฏ ูููุงูุฏ\
    \n\n**โฎโขโ ุงูุงููุฑ โฆ **`.ุณุงููุฏ` ุจุงูุฑุฏ ุนูู ุงูุฑุงุจุท\
    \n**ุงูุดูุฑุญ โขโข **ุชุญููู ููุงุทูุน ุงูููุฏููู ูู ุณูุงููุฏ ูููุงูุฏ"
    }
)
