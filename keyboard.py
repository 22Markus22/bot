from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)

keyboard1 = [
    [
        KeyboardButton(text='Оплата урока'),
        KeyboardButton(text='Связь с учителем')
    ],
    [
        KeyboardButton(text='Youtube канал для обзора курса', url='https://www.youtube.com/?ysclid=m1kwece6y4248544405'),
        KeyboardButton(text='', callback_data='value')
    ]
]

roleOfUser = [
    [
        KeyboardButton(text='Ученик'),
        KeyboardButton(text='Родитель')
    ]
]

choose_role: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=roleOfUser,
    one_time_keyboard=True,
    resize_keyboard=True
)

keyboards = ReplyKeyboardMarkup(
    keyboards=keyboard1
)