import requests
import asyncio
import os

from enum import Enum
from dotenv import load_dotenv
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram import F, Router 
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Handlers.keyboards import (yes_no, 
                                start_kb,
                                priority_index,
                                task_kb,
                                myTasks_kb)

# TODO: важность задачи.

router = Router()
load_dotenv()
URL = os.getenv('BASE_URL')

priority_status = ["Обычный 🌑", 
                    "Средний 🌒", 
                    "Высокий 🌓"]

precedence = {
    "Обычный 🌑": "DEFAULT",
    "Средний 🌒": "MEDIUM",
    "Высокий 🌓": "HIGH"
}

class executionStatus(Enum):
    DO = 1
    DOING = 2
    DONE = 3

class Form(StatesGroup):
    user_id = State()
    name = State()
    description = State()
    priority = State()
    taskState = State()
    check = State()
    upload = State()
    back = State()

@router.message(F.text == "Задачи📗")
async def keyboard(message: Message):
    await message.answer("Приветствую тебя в панели задач!\n\n"
                         "Хочешь посмотреть... А может создать новую задачу!?\n\n"
                         "Для выхода из диалога, введите /back во время проверки на корректность!", reply_markup=task_kb)

@router.message(F.text == "Новая задача📕")
async def task(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer('Какую задачу я должен установить?', reply_markup=ReplyKeyboardRemove())

@router.message(Form.name)
async def desc(message: Message, state: FSMContext):
    await state.update_data(name=message.text, user_id=message.from_user.id)
    await state.set_state(Form.description)
    await message.answer('Опишите установленную задачу!')

@router.message(Form.description)
async def index(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(Form.priority)
    await message.answer('Выберите приоритет задачи!', reply_markup=priority_index)

@router.message(Form.priority)
async def verify(message: Message, state: FSMContext):
    
    await state.update_data(priority=message.text)
    data = await state.get_data()
    priority = data.get("priority")

    if priority not in priority_status:
        priority = priority_status[0]

    verifying = "Давайте проверим всё ли верно!\n\n" \
              f"Задача: {data.get("name")}\n" \
              f"Описание: {data.get("description")}\n" \
              f"Приоритет: {priority}"
    
    await message.answer(verifying, reply_markup=yes_no)
    await state.set_state(Form.check)
    
@router.callback_query(F.data == "correct", Form.check)
async def correct(call: CallbackQuery, state: FSMContext):
    await state.update_data(taskState=executionStatus.DOING.name)
    data = await state.get_data()
    await upload(data=data)
    await call.message.answer("Задача была создана!", reply_markup=start_kb)
    await call.answer()
    await state.clear()

@router.callback_query(F.data == "incorrect", Form.check)
async def incorrect(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Хорошо, заполним задачу заново!\n\n" \
                              "Какую задачу я должен установить?")
    await state.set_state(Form.name)
    await call.answer()

@router.message(F.text == "🔙 Выход")
async def leave(message: Message, state: FSMContext):
    await message.answer("До новых встреч, приятель!", reply_markup=start_kb)
    await state.set_state(None)

@router.message(F.text == "Мои задачи📚")
async def myTasks(message: Message):
    await message.answer("Выберите приоритет задач!", reply_markup=myTasks_kb)

@router.callback_query(F.data == "DEFAULT" or "MEDIUM" or "HIGH")
async def defaultCategory(call: CallbackQuery):
    user_id = call.from_user.id
    if call.data in precedence.keys():
        priority = precedence.get(call.data)
    else:
        priority = precedence.get(priority_status[0])
        
    obj = {
        "userId": user_id,
        "priority": priority
    }

    getTaskList(obj=obj)


async def getTaskList(obj):
    getTask = requests.get(f"{URL}/task", json=obj)
    jsonTask = getTask.json()
    for i in len(jsonTask):
        None

async def upload(data):
    user_id = data.get("user_id")
    name = data.get("name")
    description = data.get("description")
    currentState = data.get("taskState")
    if data.get("priority") in precedence.keys():
        priority = precedence.get(data.get("priority"))
    else:
        priority = precedence.get(priority_status[0])
            
    # Don't uncomment till the server is on
    
    obj = {
        "userId": user_id,
        "name": name,
        "description": description,
        "priority": priority,
        "state": currentState
    }

    requests.post(f"{URL}/task", json=obj)