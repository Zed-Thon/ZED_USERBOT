#๐๐๐๐๐๐ค๐ฃ ยฎ
#ุงููููู ุญูููู ููุชุงุจูุฉ ุฒููุฒุงู ุงูููุจูู โคถ @zzzzl1l ุฎุงุต ุจุณููุฑุณ โคถ ๐๐๐๐๐๐ค๐ฃ
#ุงูููู ูู ุจุงูุซูู ููููุง ุฎูุทุช ุฑุงุญ ุชุทูุน ุญููููููููู ุจุณูููุฑุณูููู

#ูููููููููููููููููู


import os
from faker import Faker
import datetime
from telethon import functions, types, events
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest

from ..utils import admin_cmd, sudo_cmd

from . import reply_id


@bot.on(admin_cmd(pattern="ูุงุดู ?(.*)"))
@bot.on(sudo_cmd(pattern="ูุงุดู ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**โฎ . ููุงุดู ุงูุงเขชููุงู ุงููุูเขชุจููุฉ ๐ฒ.. ุงุฑเขชุณูู .ู34 ููุชุนููููุงุช ๐ซโฐ**"
        )
    chat = "@Zelzalybot"
    catevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑูู ุงูููุดู ุููู ุงููุฑููู  ๐ฒโญ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1194140165)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @Zelzalybot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)



CMD_HELP.update(
    {
        "ุงููุงุดู": "**ุงุณู ุงูุงุถุงููู : **`ุงููุงุดู`\
    \n\n**โฎโขโ ุงูุงููุฑ โฆ **`.ูุงุดู`  \
    \n**ุงูุดูุฑุญ โขโข **ููุงุดู ุงูุงุฑููุงู ุงูุนูุฑุจููุฉ ๐ฒ .. ุงููุญููุฏ ุน ุชูููุฌูุฑุงู .. ุงุฑุณูู .ูุงุดู"
    }
)
