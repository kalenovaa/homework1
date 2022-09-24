import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="lol")


async def go_lesson():
    await bot.send_message(chat_id=chat_id, text="beach go to the lesson")


async def lesson():
    await bot.send_message(chat_id=chat_id, text='go to the lesson')


async def scheduler():
    aioschedule.every().monday.at("17:00").do(lesson)
    aioschedule.every().thursday.at("17:00").do(go_lesson)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'напомни' in word.text)