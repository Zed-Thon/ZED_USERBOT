#๐๐๐๐๐๐ค๐ฃ ยฎ
#ุงููููู ุญูููู ููุชุงุจูุฉ ุฒููุฒุงู ุงูููุจูู " ุดุฎุตููุงู " ููุงููุฌูุฏ ูุง  ุณูุฑุณ ุงุฌูุจูู ููุง ุนูุฑุจู โคถ @zzzzl1l ุฎุงุต ุจุณููุฑุณ โคถ ๐๐๐๐๐๐ค๐ฃ
#ุชุฎููุท ููุงุชุฐููุฑ ุงูุญูููู ุงููููู

from userbot.Config import Config
import asyncio

import requests
from telethon import functions
from . import *
from . import ALIVE_NAME


import requests
from telethon import functions
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot, BotInlineDisabledError as noinline, YouBlockedUserError

botname = Config.TG_BOT_USERNAME

@bot.on(admin_cmd(pattern="ุงููุงูู ุชูุนูู ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="ุงููุงูู ุชูุนูู ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USERNAME
    chat = "@Botfather"
    if tgbotusername is not None:
        try:
            results = await event.client.inline_query(tgbotusername, "Zelzal_Ahmed")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except:
            zelzal = await eor(event, "**โโุฌูุงุฑู ุงูุงุชุตูุงู ุจุจููุช ููุงุฐุฑ ...โฃ**\n**โโุชูู ุชูุนููู ุงูููุงูู ุจููุชู .. ุจูุฌูุงุญ โ๏ธ**\n\n**โโุฌูุงุฑู ุงุนูุงุฏุฉ ุชุดุบูู ุงูุจููุช ุงูุฑุฌูุงุก ุงูุงูุชุธูุงุฑ  โฌโญ...๐ซ**")
            async with bot.conversation(chat) as conv:
                try:
                    first = await conv.send_message("/setinline")
                    second = await conv.get_response()
                    third = await conv.send_message(tgbotusername)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message("ZedThon")
                    sixth = await conv.get_response()
                    seventh = await conv.send_message(perf)
                    eighth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await zelzal.edit("**โโููู ุจุฅูุบูุงุก ุงูุญุธูุฑ ุนูู ุจููุช ููุงุฐุฑ ุงููุง @Botfather .. ุซูู ุงุนูุฏ ุงููุญูุงููู**")
                await bot.edit(f"**โโุชูู ุชูุนููู ุงูููุงูู ุจููุชู .. ุจูุฌูุงุญ โ๏ธ**")
            await bot.delete_messages(
                conv.chat_id, [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id]
            )
    else:
        await eor(event, "**โโูููุงูู ุฎุทูุฃ!!โ?๏ธ**\n**โโุงููุฑุฌุงุก ุงูุชุญููู ููู ููุงุฑุงุช TG_BOT_TOKEN & TG_BOT_USERNAME ุนููู ูููุฑูููู ...โฃ**")


@bot.on(admin_cmd(pattern="ุงููุงูู ุชุนุทูู ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="ุงููุงูู ุชุนุทูู ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USERNAME
    chat = "@Botfather"
    if tgbotusername is not None:
        try:
            results = await event.client.inline_query(tgbotusername, "Zelzal_Ahmed")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except:
            zelzal = await eor(event, "**โโุฌูุงุฑู ุงูุงุชุตูุงู ุจุจููุช ููุงุฐุฑ ...โฃ**\n**โโุชูู ุชุนุทููู ุงูููุงูู ุจููุชู .. ุจูุฌูุงุญ โ๏ธ**\n\n**โโุฌูุงุฑู ุงุนูุงุฏุฉ ุชุดุบูู ุงูุจููุช ุงูุฑุฌูุงุก ุงูุงูุชุธูุงุฑ  โฌโญ...๐ซ**")
            async with bot.conversation(chat) as conv:
                try:
                    first = await conv.send_message("/setinline")
                    second = await conv.get_response()
                    third = await conv.send_message(tgbotusername)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message("/empty")
                    sixth = await conv.get_response()
                    seventh = await conv.send_message(perf)
                    eighth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await zelzal.edit("**โโููู ุจุฅูุบูุงุก ุงูุญุธูุฑ ุนูู ุจููุช ููุงุฐุฑ ุงููุง @Botfather .. ุซูู ุงุนูุฏ ุงููุญูุงููู**")
                await bot.edit(f"**โโุชูู ุชุนุทููู ุงูููุงูู ุจููุชู .. ุจูุฌูุงุญ โ๏ธ**")
            await bot.delete_messages(
                conv.chat_id, [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id]
            )
    else:
        await eor(event, "**โโูููุงูู ุฎุทูุฃ!!โ?๏ธ**\n**โโุงููุฑุฌุงุก ุงูุชุญููู ููู ููุงุฑุงุช TG_BOT_TOKEN & TG_BOT_USERNAME ุนููู ูููุฑูููู ...โฃ**")



@bot.on(admin_cmd(pattern="ุชุนููู ูุจุฐุฉ ุงูุจูุช ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="ุชุนููู ูุจุฐุฉ ุงูุจูุช ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USERNAME
    chat = "@Botfather"
    if tgbotusername is not None:
        try:
            results = await event.client.inline_query(tgbotusername, "Zelzal_Ahmed")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except:
            zelzal = await eor(event, "**โโุฌูุงุฑู ุงูุงุชุตูุงู ุจุจููุช ููุงุฐุฑ ...โฃ**\n**โโุงุฑุณูู ุงูุงููุฑ ุงูุชูุงูู ูููุถุน ุงููุจุฐุฉ โ๏ธ**\n\n**โโ.ูุถุน ูุจุฐุฉ + ูุจุฐุชูู ...๐ซ**")
            async with bot.conversation(chat) as conv:
                try:
                    first = await conv.send_message("/setabouttext")
                    second = await conv.get_response()
                    third = await conv.send_message(tgbotusername)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message(perf)
                    sixth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await zelzal.edit("**โโููู ุจุฅูุบูุงุก ุงูุญุธูุฑ ุนูู ุจููุช ููุงุฐุฑ ุงููุง @Botfather .. ุซูู ุงุนูุฏ ุงููุญูุงููู**")
                await bot.edit(f"**โโุชูู ุชูุนููู ูุจูุฐุฉ ุจููุชู .. ุจูุฌูุงุญ โ๏ธ**")
            await bot.delete_messages(
                conv.chat_id, [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id]
            )
    else:
        await eor(event, "**โโูููุงูู ุฎุทูุฃ!!โ?๏ธ**\n**โโุงููุฑุฌุงุก ุงูุชุญููู ููู ููุงุฑุงุช TG_BOT_TOKEN & TG_BOT_USERNAME ุนููู ูููุฑูููู ...โฃ**")


@bot.on(admin_cmd(pattern="ุชุนููู ูุตู ุงูุจูุช ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="ุชุนููู ูุตู ุงูุจูุช ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USERNAME
    chat = "@Botfather"
    if tgbotusername is not None:
        try:
            results = await event.client.inline_query(tgbotusername, "Zelzal_Ahmed")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except:
            zelzal = await eor(event, "**โโุฌูุงุฑู ุงูุงุชุตูุงู ุจุจููุช ููุงุฐุฑ ...โฃ**\n**โโุงุฑุณูู ุงูุงููุฑ ุงูุชูุงูู ูููุถุน ุงููุตู โ๏ธ**\n\n**โโ.ูุถุน ูุตู + ูุตููู ...๐ซ**")
            async with bot.conversation(chat) as conv:
                try:
                    first = await conv.send_message("/setdescription")
                    second = await conv.get_response()
                    third = await conv.send_message(tgbotusername)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message(perf)
                    sixth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await zelzal.edit("**โโููู ุจุฅูุบูุงุก ุงูุญุธูุฑ ุนูู ุจููุช ููุงุฐุฑ ุงููุง @Botfather .. ุซูู ุงุนูุฏ ุงููุญูุงููู**")
                await bot.edit(f"**โโุชูู ุชูุนููู ูุตูู ุจููุชู .. ุจูุฌูุงุญ โ๏ธ**")
            await bot.delete_messages(
                conv.chat_id, [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id]
            )
    else:
        await eor(event, "**โโูููุงูู ุฎุทูุฃ!!โ?๏ธ**\n**โโุงููุฑุฌุงุก ุงูุชุญููู ููู ููุงุฑุงุช TG_BOT_TOKEN & TG_BOT_USERNAME ุนููู ูููุฑูููู ...โฃ**")


@bot.on(admin_cmd(pattern="ุชุนููู ุงุณู ุงูุจูุช ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="ุชุนููู ุงุณู ุงูุจูุช ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USERNAME
    chat = "@Botfather"
    if tgbotusername is not None:
        try:
            results = await event.client.inline_query(tgbotusername, "Zelzal_Ahmed")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except:
            zelzal = await eor(event, "**โโุฌูุงุฑู ุงูุงุชุตูุงู ุจุจููุช ููุงุฐุฑ ...โฃ**\n**โโุงุฑุณูู ุงูุงููุฑ ุงูุชูุงูู ูููุถุน ุงูุงุณู โ๏ธ**\n\n**โโ.ูุถุน ุงุณู + ุงุณูู ุงูุจููุช ...๐ซ**")
            async with bot.conversation(chat) as conv:
                try:
                    first = await conv.send_message("/setname")
                    second = await conv.get_response()
                    third = await conv.send_message(tgbotusername)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message(perf)
                    sixth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await zelzal.edit("**โโููู ุจุฅูุบูุงุก ุงูุญุธูุฑ ุนูู ุจููุช ููุงุฐุฑ ุงููุง @Botfather .. ุซูู ุงุนูุฏ ุงููุญูุงููู**")
                await bot.edit(f"**โโุชูู ุชูุนููู ุงุณูู ุจููุชู .. ุจูุฌูุงุญ โ๏ธ**")
            await bot.delete_messages(
                conv.chat_id, [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id]
            )
    else:
        await eor(event, "**โโูููุงูู ุฎุทูุฃ!!โ?๏ธ**\n**โโุงููุฑุฌุงุก ุงูุชุญููู ููู ููุงุฑุงุช TG_BOT_TOKEN & TG_BOT_USERNAME ุนููู ูููุฑูููู ...โฃ**")


@bot.on(admin_cmd(pattern="ุชุนููู ุตูุฑุฉ ุงูุจูุช ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="ุชุนููู ุตูุฑุฉ ุงูุจูุช ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USERNAME
    chat = "@Botfather"
    if tgbotusername is not None:
        try:
            results = await event.client.inline_query(tgbotusername, "Zelzal_Ahmed")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except:
            zelzal = await eor(event, "**โโุฌูุงุฑู ุงูุงุชุตูุงู ุจุจููุช ููุงุฐุฑ ...โฃ**\n**โโุงุฑุณูู ุงูุงููุฑ ุงูุชูุงูู ูููุถุน ุงูุตูุฑุฉ โ๏ธ**\n\n**โโ.ูุถุน ุตูุฑุฉ ุจุงููุฑุฏ ุนููู ุตููุฑุฉ ...๐ซ**")
            async with bot.conversation(chat) as conv:
                try:
                    first = await conv.send_message("/setuserpic")
                    second = await conv.get_response()
                    third = await conv.send_message(tgbotusername)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message(perf)
                    sixth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await zelzal.edit("**โโููู ุจุฅูุบูุงุก ุงูุญุธูุฑ ุนูู ุจููุช ููุงุฐุฑ ุงููุง @Botfather .. ุซูู ุงุนูุฏ ุงููุญูุงููู**")
                await bot.edit(f"**โโุชูู ุชูุนููู ุตููุฑุฉ ุจููุชู .. ุจูุฌูุงุญ โ๏ธ**")
            await bot.delete_messages(
                conv.chat_id, [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id]
            )
    else:
        await eor(event, "**โโูููุงูู ุฎุทูุฃ!!โ?๏ธ**\n**โโุงููุฑุฌุงุก ุงูุชุญููู ููู ููุงุฑุงุช TG_BOT_TOKEN & TG_BOT_USERNAME ุนููู ูููุฑูููู ...โฃ**")



#๐๐๐๐๐๐ค๐ฃ ยฎ
#ุงููููู ุญูููู ููุชุงุจูุฉ ุฒููุฒุงู ุงูููุจูู " ุดุฎุตููุงู " ููุงููุฌูุฏ ูุง  ุณูุฑุณ ุงุฌูุจูู ููุง ุนูุฑุจู โคถ @zzzzl1l ุฎุงุต ุจุณููุฑุณ โคถ ๐๐๐๐๐๐ค๐ฃ
#ุชุฎููุท ููุงุชุฐููุฑ ุงูุญูููู ุงููููู

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from PIL import Image
from userbot.utils import sudo_cmd

from . import reply_id


@bot.on(admin_cmd(pattern="ูุถุน ูุจุฐุฉ ?(.*)"))
@bot.on(sudo_cmd(pattern="ูุถุน ูุจุฐุฉ ?(.*)", allow_sudo=True))
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
            event, "**โฎ ูุชุบูููุฑ ูุจูุฐุฉ ุจูุชูู ุงููุณูุงุนุฏ ุจุฏูู ุงูุฐูุงุจ ูุจูุช ููุงุฐุฑ ุงุฑุณูู .ูุถุน ูุจุฐุฉ + ุงููุจุฐุฉ ...๐ซโฐ**"
        )
    chat = "@Botfather"
    catevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุงูุงุชุตูุงู ุจุจููุช ููุงุฐุฑ ููุถูุน ุงููุจูุฐุฉ ูู ุจูุชูู ... ๐งธ๐**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=93372553)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @Botfather .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@bot.on(admin_cmd(pattern="ูุถุน ูุตู ?(.*)"))
@bot.on(sudo_cmd(pattern="ูุถุน ูุตู ?(.*)", allow_sudo=True))
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
            event, "**โฎ ูุชุบูููุฑ ูุตูู ุจูุชูู ุงููุณูุงุนุฏ ุจุฏูู ุงูุฐูุงุจ ูุจูุช ููุงุฐุฑ ุงุฑุณูู .ูุถุน ูุตู + ุงููุตู ...๐ซโฐ**"
        )
    chat = "@Botfather"
    catevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุงูุงุชุตูุงู ุจุจููุช ููุงุฐุฑ ููุถูุน ุงููุตูู ูู ุจูุชูู ... ๐งธ๐**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=93372553)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @Botfather .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@bot.on(admin_cmd(pattern="ูุถุน ุงุณู ?(.*)"))
@bot.on(sudo_cmd(pattern="ูุถุน ุงุณู ?(.*)", allow_sudo=True))
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
            event, "**โฎ ูุชุบูููุฑ ุงุณูู ุจูุชูู ุงููุณูุงุนุฏ ุจุฏูู ุงูุฐูุงุจ ูุจูุช ููุงุฐุฑ ุงุฑุณูู .ูุถุน ุงุณู + ุงุณู ุงูุจููุช ...๐๐ซโฐ**"
        )
    chat = "@Botfather"
    catevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุงูุงุชุตูุงู ุจุจููุช ููุงุฐุฑ ููุถูุน ุงูุงุณูู ูู ุจูุชูู ... ๐งธ๐**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=93372553)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @Botfather .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@bot.on(admin_cmd(pattern="ูุถุน ุตูุฑุฉ$", outgoing=True))
@bot.on(sudo_cmd(pattern="ูุถุน ุตูุฑุฉ$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**โฎ .ูุถุน ุตูุฑุฉ ุจุงููุฑุฏ ๏ฎผุ ุงูููุตููุฑฺพ? ููุถุนููุง ุจูุฑููุงููู ุจููุชู ุงููุณูุงุนูุฏ ...๐๐ซโฐ**")
        return
    chat = "@Botfather"
    catevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุงูุงุชุตูุงู ุจุจููุช ููุงุฐุฑ ููุถูุน ุจุฑูููุงูู ูู ุจูุชูู ... ๐๐**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=93372553)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @Botfather .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**๐คจ๐...ุ**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)



CMD_HELP.update(
    {
        "ุจูุช ูุงุฐุฑ": """**ุงุณูู ุงูุงุถูุงููู : **`ุจูุช ูุงุฐุฑ`
        
**โฎโขโ ุงูุงููุฑ ุชุนููู ูุชูุนูู ุจูุช ููุงุฐุฑ ูุจููุชู ุจุณูููููุฉ ุจูุฏูู ุงูุฐููุงุจ ูุจููุช ููุงุฐุฑ โฆ **


  โข  `.ุงููุงูู ุชูุนูู`

  โข  `.ุงููุงูู ุชุนุทูู`
  
  โข  `.ุชุนููู ุงุณู ุงูุจูุช`
  
  โข  `.ุชุนููู ูุจุฐุฉ ุงูุจูุช`
  
  โข  `.ุชุนููู ูุตู ุงูุจูุช`
  
  โข  `.ุชุนููู ุตูุฑุฉ ุงูุจูุช`


**ูููุณููุฎ : ** __ุงุถุบุท ุน ุงูุงููุฑ ููุณุฎูู__"""
    }
)
