import requests
import os

from dotenv import load_dotenv
from datetime import datetime
from zoneinfo import ZoneInfo
from aiogram.types import Message, callback_query, CallbackQuery
from aiogram.filters import Command
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Handlers.keyboards import (timezone_kb,
                                 tz_page_1,
                                 tz_page_2,
                                 tz_page_3,
                                 start_kb,
                                 CallbackGet )

# TODO: Добавить переход на прошлую страницу(DONE: Но лучше будет сделать через функцию),
#       установку часового пояса (UTC+?, Время в часах)

router = Router()

URL = os.getenv("BASE_URL")
class Form(StatesGroup):
    tzp1 = State()
    tzp2 = State()
    tzp3 = State()
    pv1 = State()
    pv2 = State()

timezones = ['Europe/Kaliningrad', 
             'Europe/Moscow', 'Europe/Kirov', 'Europe/Volgograd', 
             'Europe/Astrakhan', 'Europe/Saratov', 
             'Europe/Ulyanovsk', 'Europe/Samara', 
             'Asia/Yekaterinburg', 'Asia/Omsk', 
             'Asia/Novosibirsk', 'Asia/Barnaul', 
             'Asia/Tomsk', 'Asia/Novokuznetsk', 
             'Asia/Krasnoyarsk', 'Asia/Irkutsk', 
             'Asia/Chita', 'Asia/Yakutsk', 
             'Asia/Khandyga', 'Asia/Vladivostok', 
             'Asia/Ust-Nera', 'Asia/Magadan', 
             'Asia/Sakhalin', 'Asia/Srednekolymsk', 
             'Asia/Kamchatka', 'Asia/Anadyr']

@router.message(F.text == "Настройки ⚙️")
async def settings(message: Message):
    await message.answer("Выберите опцию!", reply_markup=timezone_kb)

@router.message(F.text == "Часовой-пояс 🌏")
async def set_timezone(message: Message, state: FSMContext):
    await state.set_state(Form.tzp1)
    await message.answer("Выберите часовой-пояс!\n\n"
                         "Выбрана страница 1️⃣\n\n"
                         "Для возврата в начальное меню, введите /back", 
                         reply_markup=tz_page_1)

@router.callback_query(F.data == "page2")
async def set_timezone(call: CallbackQuery, state: FSMContext):
    await state.update_data(tzp1=0)
    await state.set_state(Form.tzp2)
    await call.message.edit_text("Выберите часовой-пояс!\n\n"
                                 "Выбрана страница 2️⃣\n\n"
                                 "Для возврата в начальное меню, введите /back", 
                                 reply_markup=tz_page_2)

@router.callback_query(F.data == "page3")
async def set_timezone(call: CallbackQuery, state: FSMContext):
    await state.update_data(tzp2=1)
    await state.set_state(Form.tzp3)
    await call.message.edit_text("Выберите часовой-пояс!\n\n"
                                 "Выбрана страница 3️⃣\n\n"
                                 "Для возврата в начальное меню, введите /back", 
                                 reply_markup=tz_page_3)

@router.callback_query(F.data == "backto2")
async def previous_page1(callback: CallbackQuery):
    await callback.message.edit_text("Выберите часовой-пояс!\n\n"
                                     "Выбрана страница 2️⃣\n\n"
                                     "Для возврата в начальное меню, введите /back",
                                     reply_markup=tz_page_2)

@router.callback_query(F.data == "backto1")
async def previous_page2(callback: CallbackQuery):
    await callback.message.edit_text("Выберите часовой-пояс!\n\n"
                                     "Выбрана страница 1️⃣\n\n"
                                     "Для возврата в начальное меню, введите /back",
                                     reply_markup=tz_page_1)

@router.callback_query()
async def test(call: CallbackQuery):
    tz = call.data
    if tz in timezones:
        ready_timezone = str(datetime.now(tz=ZoneInfo(f"{tz}")))
        split_timezone_utc_server = ready_timezone[27:-3]
        split_timezone_utc = ready_timezone[27:]
        split_timezone_current = ready_timezone[:-13]
        await call.message.answer(f"Установлено ваше смещение по UTC: {split_timezone_utc} ⌚")
        await call.message.answer(f"Ваше текущее время: {split_timezone_current} ⌚")

        user_id = call.from_user.id
        
        requests.put(f"{URL}/user/{user_id}/utc/{split_timezone_utc_server}")

        await call.answer()

@router.message(F.text == "/back")
async def set_timezone(message: Message):
    await message.answer("Выбрано начальное меню...", reply_markup=start_kb)