from create_bot import bot, dp
from aiogram import Bot, Dispatcher, executor, types
from handlers import admin, client

import asyncio
import handlers.tools as tools
from sqlighter import Database


# update statistic
async def update_data(whait_for=3600):
    while True:
        db = Database()
        db.update_data()
        await asyncio.sleep(whait_for)


async def start_bot(_):
    me = await bot.get_me()
    print(f"""\n--------------------------
Bot {me.first_name} start
--------------------------\n""")

    # async run bot and update static
if __name__ == "__main__":
    admin.register_handlers(dp=dp)  # необходимо для корректной работы handlers
    client.register_handlers(dp=dp)
    asyncio.get_event_loop().create_task(update_data(10800))
    executor.start_polling(dp, on_startup=start_bot, skip_updates=True)
