import asyncio
import getpass
import os

from dotenv import load_dotenv
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F

from Handlers.keyboards import admin_kb

load_dotenv()
router = Router()

PW = os.getenv("ADMIN")

auth = 0

@router.message(F.text == "!admin")
async def Admin(message: Message):
    password = message.answer(getpass.getpass("Enter the PASSWORD: "))
    if password.text == PW:
        await message.answer("welcome to the Admin-Panel", reply_markup=admin_kb)
        global auth
        auth += 1
    else:
        await message.answer("ERROR: You're not the Admin ...")

@router.message(F.text == "cls")
async def Admin(message: Message):
    if auth == 1:
        None
