from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
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
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите опцию...",
    selective=True,
    one_time_keyboard=True
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