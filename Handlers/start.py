import asyncio
import requests

from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F

from Handlers.keyboards import start_kb

router = Router()

@router.message(F.text == "/start")
async def Start(message: Message):
    # user_id = message.from_user.id
    await message.answer(f"Добро пожаловать в бота для заметок log!\nГотов освобождать голову для новых идей?", reply_markup=start_kb)