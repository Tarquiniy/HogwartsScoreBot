from aiogram import Router, Bot, F, Dispatcher
from aiogram.types import Message, CallbackQuery
from settings import settings
import keyboards as kb
import json


dp= Dispatcher()
router = Router()
router.message.filter(F.chat.type == "private")
bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')


@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer(f'Приветствую,{message.from_user.first_name}. Выберите пункт меню', reply_markup=kb.main)


@router.message(F.text == 'Выбрать факультет')
async def catalog(message: Message):
    await message.answer('Выберите категорию', reply_markup=kb.facultets)


@router.callback_query(F.data == 'Гриффиндор')
async def Griffindor(callback: CallbackQuery):
    await callback.message.answer(f'Что вы хотите сделать?', reply_markup=kb.change_score)


@router.callback_query(F.data == 'Слизерин')
async def Sliseryn(callback: CallbackQuery):
    await callback.message.answer(f'Что вы хотите сделать?', reply_markup=kb.change_score)


@router.callback_query(F.data == 'Хаффлпафф')
async def Hufflpuff(callback: CallbackQuery):
    await callback.message.answer(f'Что вы хотите сделать?', reply_markup=kb.change_score)


@router.callback_query(F.data == 'Рейвенкло')
async def Ravenclaw(callback: CallbackQuery):
    await callback.message.answer(f'Что вы хотите сделать?', reply_markup=kb.change_score)


def add_to_points(points: int):
    global data
    data["Гриффиндор"] = data["Гриффиндор"] + points if "Гриффиндор" in data else points


@router.callback_query(F.data == 'Добавить баллы')
async def Add_Score(callback: CallbackQuery):
    await callback.message.answer(f'Введите количество баллов')
    with open('score.json', 'r', encoding='utf-8') as json_file:
        change_score = json.load(json_file)
        change_score["facultets"][0]['Баллов'] += {callback.text}
    with open('score.json', 'w', encoding='utf-8') as json_file:
        json.dump(change_score, json_file, ensure_ascii=False, indent=4)



@router.callback_query(F.data == 'Отнять баллы')
async def Add_Score(callback: CallbackQuery):
    await callback.message.answer(f'Введите количество баллов')


@router.message()
async def echo(message: Message):
    await message.answer(f'Моя твоя не понимать, {message.from_user.first_name}')
