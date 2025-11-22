import asyncio
import requests
import os

from dotenv import load_dotenv
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F

from Handlers.keyboards import start_kb

load_dotenv()
URL = os.getenv('BASE_URL')

router = Router()

@router.message(F.text == "/start")
async def Start(message: Message):
    user_id = message.from_user.id
    await message.answer(f"Добро пожаловать в бота для заметок log!\nГотов освобождать голову для новых идей?", reply_markup=start_kb)

    try:

        obj = {
            "tgId": user_id      
            }
        
        await requests.post(f"{URL}/user", json=obj)

    except:
        print("ID can't be accessed")