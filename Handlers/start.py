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

    # Don't uncomment till the server is on

    # try:
    #     state = requests.get(f"{URL}/user/tg/{user_id}")
    #     if state.status_code == 404:
    #         obj = {
    #             "tgId": user_id
    #         }
    #         requests.post(f"{URL}/{user_id}", json=obj)
    # except:
    #     print("can't process the request...")