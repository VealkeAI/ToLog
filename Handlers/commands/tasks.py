import requests
import asyncio
import os

from dotenv import load_dotenv
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram import F, Router 
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Handlers.keyboards import yes_no, start_kb

# TODO: Добавить возможность изменить задачу, важность задачи.

router = Router()
load_dotenv()
URL = os.getenv('BASE_URL')

unic_num = 0

class Form(StatesGroup):
    user_id = State()
    name = State()
    description = State()
    check = State()
    upload = State()

@router.message(F.text == "Задачи📗")
async def task(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Form.name)
    await message.answer('Какую задачу я должен установить?')

@router.message(Form.name)
async def desc(message: Message, state: FSMContext):
    await state.update_data(name=message.text, user_id=message.from_user.id)
    await state.set_state(Form.description)
    await message.answer('Опишите установленную задачу!')

@router.message(Form.description)
async def verify(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    data = await state.get_data()

    verifying = "Давайте проверим всё ли верно!\n\n" \
              f"Ваш ID: {data.get("user_id")}\n" \
              f"Задача: {data.get("name")}\n" \
              f"Описание: {data.get("description")}"
    
    await message.answer(verifying, reply_markup=yes_no)
    await state.set_state(Form.check)
    
@router.callback_query(F.data == "correct", Form.check)
async def check(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await upload(data=data)
    await call.message.answer("Задача была создана!", reply_markup=start_kb)
    await call.answer()

@router.callback_query(F.data == "incorrect", Form.check)
async def check(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Хорошо, заполним задачу заново!\n\n" \
                              "Какую задачу я должен установить?")
    await state.set_state(Form.name)
    
async def upload(data):
    user_id = data.get("user_id")
    name = data.get("name")
    description = data.get("description")

    obj = {
        "userId": user_id,
        "name": name,
        "description": description
    }

    requests.post(f"{URL}/task", json=obj)