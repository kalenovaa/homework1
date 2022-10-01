from aiogram.utils import executor
from config import bot, dp
import logging
from handlers import admin, callback, client, extra, fsm_menu, notfications, inline
from database.bot_db import sql_create
import asyncio


async def on_startup(_):
    asyncio.create_task(notfications.scheduler())
    sql_create()

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsm_menu.register_handlers_fsm_menu(dp)
notfications.register_handlers_notification(dp)
inline.register_inline_handler(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)