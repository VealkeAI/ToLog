from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)

from aiogram.filters.callback_data import CallbackData

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
            KeyboardButton(text="Настройки ⚙️")
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
            KeyboardButton(text="Часовой-пояс 🌏")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите опцию...",
    selective=True,
    one_time_keyboard=True
)

class CallbackGet(CallbackData, prefix='time'):
    action: str
    city: str

tz_page_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Europe/Kaliningrad", callback_data="Europe/Kaliningrad"),
            InlineKeyboardButton(text="Europe/Moscow", callback_data="Europe/Moscow"),
            InlineKeyboardButton(text="Europe/Kirov", callback_data="Europe/Kirov")
        ],
        [
            InlineKeyboardButton(text="Europe/Volgograd", callback_data="Europe/Volgograd"),
            InlineKeyboardButton(text="Europe/Astrakhan", callback_data="Europe/Astrakhan"),
            InlineKeyboardButton(text="Europe/Saratov", callback_data="Europe/Saratov")
        ],
        [
            InlineKeyboardButton(text="Europe/Ulyanovsk", callback_data="Europe/Ulyanovsk"),
            InlineKeyboardButton(text="Europe/Samara", callback_data="Europe/Samara"),
            InlineKeyboardButton(text="Asia/Yekaterinburg", callback_data="Asia/Yekaterinburg")
        ], 
        [
            InlineKeyboardButton(text="Следующая страница 🔜", callback_data="page2")
        ]
    ],
    resize_keyboard=True,
    selective=True
)

tz_page_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Asia/Omsk", callback_data="Asia/Omsk"),
            InlineKeyboardButton(text="Asia/Novosibirsk", callback_data="Asia/Novosibirsk"),
            InlineKeyboardButton(text="Asia/Barnaul", callback_data="Asia/Barnaul")
        ],
        [
            InlineKeyboardButton(text="Asia/Tomsk", callback_data="Asia/Tomsk"),
            InlineKeyboardButton(text="Asia/Novokuznetsk", callback_data="Asia/Novokuznetsk"),
            InlineKeyboardButton(text="Asia/Krasnoyarsk", callback_data="Asia/Krasnoyarsk")
        ],
        [
            InlineKeyboardButton(text="Asia/Irkutsk", callback_data="Asia/Irkutsk"),
            InlineKeyboardButton(text="Asia/Chita", callback_data="Asia/Chita"),
            InlineKeyboardButton(text="Asia/Yakutsk", callback_data="Asia/Yakutsk")
        ],
        [
            InlineKeyboardButton(text="Следующая страница 🔜", callback_data="page3")
        ],
        [
            InlineKeyboardButton(text="🔙 Прошлая страница", callback_data="backto1")
        ]
    ],
    resize_keyboard=True,
    selective=True
)

tz_page_3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Asia/Khandyga", callback_data="Asia/Khandyga"),
            InlineKeyboardButton(text="Asia/Vladivostok", callback_data="Asia/Vladivostok"),
            InlineKeyboardButton(text="Asia/Ust-Nera", callback_data="Asia/Ust-Nera")
        ],
        [
            InlineKeyboardButton(text="Asia/Magadan", callback_data="Asia/Magadan"),
            InlineKeyboardButton(text="Asia/Sakhalin", callback_data="Asia/Sakhalin"),
            InlineKeyboardButton(text="Asia/Srednekolymsk", callback_data="Asia/Srednekolymsk")
        ],
        [
            InlineKeyboardButton(text="Asia/Kamchatka", callback_data="Asia/Kamchatka"),
            InlineKeyboardButton(text="Asia/Anadyr", callback_data="Asia/Anadyr")
        ],
        [
            InlineKeyboardButton(text="🔙 Прошлая страница", callback_data="backto2")
        ]
    ],
    resize_keyboard=True,
    selective=True
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
    selective=True
)

priority_index = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Обычный 🌑"),
            KeyboardButton(text="Средний 🌒")
        ],
        [
            KeyboardButton(text="Высокий 🌓")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите приоритет!",
    selective=True
)

task_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Новая задача📕")
        ],
        [
            KeyboardButton(text="Мои задачи📚")
        ],
        [
            KeyboardButton(text="🔙 Выход")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите опцию!",
    selective=True,
    one_time_keyboard=True
)