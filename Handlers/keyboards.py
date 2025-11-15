from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="..."),
            KeyboardButton(text="...")
        ],
        [
            KeyboardButton(text="...")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="А что выберешь ты?",
    selective=True,
    one_time_keyboard=False
)