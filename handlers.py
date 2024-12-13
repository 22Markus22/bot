from aiogram import Router, types, F
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import keyboard

class Registration(StatesGroup):
    name = State()
    surname = State()
    role = State()
    tel_number = State()

router = Router()

@router.message(Registration.name)
async def registration_step_1(msg:Message, state: FSMContext):
    await state.update_data(name = msg.text)
    if  2<=len(msg.text)<=32:
        await msg.answer('Введите свою фамилию')
        await state.set_state(Registration.surname)
    else:
        await msg.answer('Некорректное имя, повторите попытку.')

@router.message(Registration.surname)
async def registration_step_2(msg:Message, state: FSMContext):
    await state.update_data(surname = msg.text)
    if  2<=len(msg.text)<=32:
        await msg.answer('Выберите свою роль', reply_markup=keyboard.choose_role)
        await state.set_state(Registration.role)
    else:
        await msg.answer('Некорректное имя, повторите попытку.')

@router.message(Registration.role)
async def registration_step_3(msg:Message, state: FSMContext):
    if (msg.text.lower() not in ['родитель','ученик']):
        await msg.answer('Неверно введена роль, повторите попытку\nВыберите роль',replay_markup=keyboard.choose_role)
        await state.set_state(Registration.role)
    else:
        await state.update_data(role = msg.text)
        await msg.answer('Введите свой номер телефона')
        await state.set_state(Registration.tel_number)

@router.message(Registration.tel_number)
async def registration_step_4(msg:Message, state: FSMContext):
    await state.update_data(tel_number = msg.text)
    if '+1234567890'.find(msg.text[0]) and msg.text[1:].isdigit():
        data = await state.get_data()
        await msg.answer('Спасибо за регистрацию!')
    else:
        await msg.answer('Неверный номер телефона, повторите попытку.')
    await state.clear()

@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer('Привет, я - Всезнайка, твой помошник на этом курсе. С моей помощью ты сможешь: \n●Отсылать задания на проверку.\n●Отвечать на вопросы по тесту.\n●Также я буду напоминать тебе о будущих занятиях, чтобы ты их точно не пропустил.\n(для получения списка комманд введи в чат /commands)')

@router.message(Command('test'))
async def start_handler(msg: Message):
    await msg.answer('Извини, в данный момент активных тестов нет, но я обязательно сообщу если они появятся!')

@router.message(Command('fact'))
async def start_handler(msg: Message):
    await msg.answer('Интересный факт: факта не будет')

@router.message(Command('keyboard'))
async def start_handler(msg: Message):
    await msg.answer('Запрос клавиатуры успешен', reply_markup=keyboard.keyboard)

@router.callback_query(F.data == 'value')
async def click_button_1(callback: CallbackQuery):
    await callback.answer(text='2222222', show_alert=True)
    await callback.message.answer('нажата кнопка 1')

@router.message(Command('registration'))
async def start_registration(msg: Message, state: FSMContext):
    await state.set_state(Registration.name)
    await msg.answer('Введите свое имя.')

@router.message(Command('commands'))
async def start_handler(msg: Message):
    await msg.answer('Список комманд: \n/start \n/registration')

@router.message()
async def message_handler(msg: Message):
    await msg.answer(f'Твой ID: {msg.from_user.id}')

