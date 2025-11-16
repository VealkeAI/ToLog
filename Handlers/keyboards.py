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
    input_field_placeholder="Выбор только твой..!",
    selective=True,
    one_time_keyboard=False
)

admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="UserID")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выбор только твой..!",
    selective=True,
    one_time_keyboard=False
)