import requests
import os
import arrow

from dotenv import load_dotenv
from datetime import datetime
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
    await message.answer("Выберите часовой-пояс!\n\n"
                         "Выбрана страница 1️⃣\n\n"
                         "Для возврата в начальное меню, введите /back", 
                         reply_markup=tz_page_1)

@router.callback_query(F.data == "page2")
async def set_timezone(call: CallbackQuery, state: FSMContext):
    await state.set_state(Form.tzp2)
    await call.message.edit_text("Выберите часовой-пояс!\n\n"
                                 "Выбрана страница 2️⃣\n\n"
                                 "Для возврата в начальное меню, введите /back", 
                                 reply_markup=tz_page_2)

@router.callback_query(F.data == "page3")
async def set_timezone(call: CallbackQuery, state: FSMContext):
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
        factory = arrow.ArrowFactory()
        time = factory.get(tzinfo=tz)

        # Used only in PUT request cuz we need a single number

        await call.message.answer(f"Выбранный регион: {tz}⌚")
        await call.message.answer(f"Установлено ваше смещение по UTC: {time.strftime("%Z:%M")}⌚")
        await call.message.answer(f"Ваше текущее время: {time.strftime("%H:%M:%S")} ⌚")

        user_id = call.from_user.id
        
        # Don't uncomment this bullshit until you want to fuck the bot up

        # try:
        #    status = requests.put(f"{URL}/user/{user_id}/utc/{time.strftime("%Z")}")
        # except:
        #     print("Не выходит доставить запрос...\n" \
        #           "Не выходит получить статус код...")

        log_time_yk = factory.get(tzinfo="Asia/Yakutsk")
        log_time_as = factory.get(tzinfo="Europe/Astrakhan")

        file_path = r"D:\Programming\ToLog-TG\logs\utcLog.txt"


        # to past when the server is on: status.status_code
        logs = f"Астрахань: {log_time_as.strftime("%H:%M:%S")}; Якутск: {log_time_yk.strftime("%H:%M:%S")}; status: 202; user: {user_id} "
        with open(file_path, 'a', encoding="utf-8") as file:
            file.write(logs)

        await call.answer()

@router.message(F.text == "/back")
async def set_timezone(message: Message):
    await message.answer("Выбрано начальное меню...", reply_markup=start_kb)