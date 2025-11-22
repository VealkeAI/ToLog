from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Планы📙"),
            KeyboardButton(text="Задачи📗")
        ],
        [
            KeyboardButton(text="Напоминания📕"),
            KeyboardButton(text="помощь📒")
        ],
        [
            KeyboardButton(text="Настройки⚙️")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите опцию...",
    selective=True,
    one_time_keyboard=False
)

admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="UserID"),
            KeyboardButton(text="UserBAN"),
            KeyboardButton(text="cls")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="root",
    selective=True,
    one_time_keyboard=False
)

set_time_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="30m"),
            KeyboardButton(text="5h")
        ],
        [
            KeyboardButton(text="1mth")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите длительность...",
    selective=True,
    one_time_keyboard=False
)

timezone_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Часовой-пояс🌏")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите настройку...",
    selective=True,
    one_time_keyboard=False
)

tz_page_1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Europe/Kaliningrad"),
            KeyboardButton(text="Europe/Moscow"),
            KeyboardButton(text="Europe/Kirov")
        ],
        [
            KeyboardButton(text="Europe/Volgograd"),
            KeyboardButton(text="Europe/Astrakhan"),
            KeyboardButton(text="Europe/Saratov")
        ],
        [
            KeyboardButton(text="Europe/Ulyanovsk"),
            KeyboardButton(text="Europe/Samara"),
            KeyboardButton(text="Asia/Yekaterinburg")
        ],
        [
            KeyboardButton(text="Страница №2")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите настройку...",
    selective=True,
    one_time_keyboard=False
)

tz_page_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Asia/Omsk"),
            KeyboardButton(text="Asia/Novosibirsk"),
            KeyboardButton(text="Asia/Barnaul")
        ],
        [
            KeyboardButton(text="Asia/Tomsk"),
            KeyboardButton(text="Asia/Novokuznetsk"),
            KeyboardButton(text="Asia/Krasnoyarsk")
        ],
        [
            KeyboardButton(text="Asia/Irkutsk"),
            KeyboardButton(text="Asia/Chita"),
            KeyboardButton(text="Asia/Yakutsk")
        ],
        [
            KeyboardButton(text="Страница №3")
        ],
        [
            KeyboardButton(text="🔙 Прошлая страница")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите настройку...",
    selective=True,
    one_time_keyboard=False
)

tz_page_3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Asia/Khandyga"),
            KeyboardButton(text="Asia/Vladivostok"),
            KeyboardButton(text="Asia/Ust-Nera")
        ],
        [
            KeyboardButton(text="Asia/Magadan"),
            KeyboardButton(text="Asia/Sakhalin"),
            KeyboardButton(text="Asia/Srednekolymsk")
        ],
        [
            KeyboardButton(text="Asia/Kamchatka"),
            KeyboardButton(text="Asia/Anadyr"),
        ],
        [
            KeyboardButton(text="❌ Отмена")
        ],
        [
            KeyboardButton(text="🔙 Прошлая страница")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите настройку...",
    selective=True,
    one_time_keyboard=False
)

yes_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Да, всё верно", callback_data="correct")
        ],
        [
            InlineKeyboardButton(text="❌ Изменить задачу", callback_data="incorrect")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите длительность...",
    selective=True
)