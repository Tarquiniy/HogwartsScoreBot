from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main_kb = [
    [KeyboardButton(text='Выбрать факультет'),
     KeyboardButton(text='Узнать количество баллов')]
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню')


facultets = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гриффиндор', callback_data='Гриффиндор'),
     InlineKeyboardButton(text='Слизерин', callback_data='Слизерин'),
     InlineKeyboardButton(text='Хаффлпафф', callback_data='Хаффлпафф'),
     InlineKeyboardButton(text='Рейвенкло', callback_data='Рейвенкло')]
])


change_score = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить баллы', callback_data='Добавить баллы'),
     InlineKeyboardButton(text='Отнять баллы', callback_data='Отнять баллы') ]
])


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)

