import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from Handlers import start
from Handlers.commands import help, tasks
from Handlers.root import admin
from Handlers.settings import timezone
from rich.console import Console

console = Console()
load_dotenv()

async def main():

    TOKEN = os.getenv('TOKEN')
    dp = Dispatcher()
    bot = Bot(TOKEN)

    dp.include_routers(
        start.router,
        tasks.router,
        timezone.router,
        admin.router,
        help.router
    )
    console.print(f"[bold blue]Bot ID: {bot.id}\n" \
                    "Bot is running...[/bold blue]")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())