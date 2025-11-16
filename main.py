import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from Handlers import start, admin

load_dotenv()

async def main():

    TOKEN = os.getenv('TOKEN')
    dp = Dispatcher()
    bot = Bot(TOKEN)

    dp.include_routers(
        start.router,
        admin.router
    )

    await dp.start_polling(bot, skip_updates="false")

if __name__ == "__main__":
    asyncio.run(main())