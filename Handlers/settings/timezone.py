from zoneinfo import ZoneInfo

from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F, Router
from Handlers.keyboards import (timezone_kb,
                                 tz_page_1,
                                 tz_page_2,
                                 tz_page_3,
                                 start_kb )

router = Router()

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

@router.message(F.text == "Настройки⚙️")
async def settings(message: Message):
    await message.answer("Выберите опцию!", reply_markup=timezone_kb)

@router.message(F.text == "Часовой-пояс🌏")
async def set_timezone(message: Message):
    await message.answer("Выберите часовой-пояс!\n\n"
                         "Выбрана страница №1..", reply_markup=tz_page_1)

@router.message(F.text == "Страница №2")
async def set_timezone(message: Message):
    await message.answer("Выбрана следующая страница...", reply_markup=tz_page_2)

@router.message(F.text == "Страница №3")
async def set_timezone(message: Message):
    await message.answer("Выбрана следующая страница...", reply_markup=tz_page_3)

@router.message(F.text == "❌ Отмена")
async def set_timezone(message: Message):
    await message.answer("Выбрано начальное меню...", reply_markup=start_kb)