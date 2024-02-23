from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter, Command
from settings import settings
import keyboards as kb
import json


router = Router()
router.message.filter(F.chat.type == "private")
bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')


available_facultets = ["Гриффиндор", "Слизерин", "Хаффлпафф", "Рейвенкло"]
available_actions = ["Добавить баллы", "Отнять баллы"]
available_menus = ["Выбрать факультет", "Узнать количество баллов"]


class Form(StatesGroup):
    start = State()
    choosing_facultet = State()
    choosing_action = State()
    choosing_action_gryf = State()
    choosing_action_slys = State()
    choosing_action_huff = State()
    choosing_action_rave = State()
    adding_score_gryf = State()
    adding_score_slys = State()
    adding_score_huff = State()
    adding_score_rave = State()
    removing_score = State()


@router.message(Command("start", "menu"))
async def cmd_menu(message: Message, state: FSMContext):
    await message.answer(
        text=f'Приветствую,{message.from_user.first_name}. Выберите пункт меню',
        reply_markup=kb.make_row_keyboard(available_menus))
    await state.set_state(Form.start)


@router.message(Form.start, F.text == "Выбрать факультет")
async def menu_chosen(message: Message, state: FSMContext):
    await message.answer(
        text="Спасибо. Теперь, пожалуйста, выберите факультет:",
        reply_markup=kb.make_row_keyboard(available_facultets)
    )
    await state.set_state(Form.choosing_facultet)


@router.message(Form.choosing_facultet, F.text == "Гриффиндор")
async def facultet_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()}.\n"
             f"Теперь выберите действие:",
        reply_markup=kb.make_row_keyboard(available_actions))
    await state.set_state(Form.choosing_action_gryf)


@router.message(Form.choosing_facultet, F.text == "Слизерин")
async def facultet_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()}.\n"
             f"Теперь выберите действие:",
        reply_markup=kb.make_row_keyboard(available_actions))
    await state.set_state(Form.choosing_action_slys)


@router.message(Form.choosing_facultet, F.text == "Хаффлпафф")
async def facultet_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()}.\n"
             f"Теперь выберите действие:",
        reply_markup=kb.make_row_keyboard(available_actions))
    await state.set_state(Form.choosing_action_huff)


@router.message(Form.choosing_facultet, F.text == "Рейвенкло")
async def facultet_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()}.\n"
             f"Теперь выберите действие:",
        reply_markup=kb.make_row_keyboard(available_actions))
    await state.set_state(Form.choosing_action_rave)


@router.message(Form.choosing_action_gryf, F.text == "Добавить баллы")
async def action_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} факультету.\n\n",
        reply_markup=kb.make_row_keyboard(available_menus)
    )
    await state.set_state(Form.adding_score_gryf)


@router.message(Form.choosing_action_slys, F.text == "Добавить баллы")
async def action_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} факультету.\n\n",
        reply_markup=kb.make_row_keyboard(available_menus)
    )
    await state.set_state(Form.adding_score_slys)


@router.message(Form.choosing_action_huff, F.text == "Добавить баллы")
async def action_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} факультету.\n\n",
        reply_markup=kb.make_row_keyboard(available_menus)
    )
    await state.set_state(Form.adding_score_huff)


@router.message(Form.choosing_action_rave, F.text == "Добавить баллы")
async def action_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} факультету.\n\n",
        reply_markup=kb.make_row_keyboard(available_menus)
    )
    await state.set_state(Form.adding_score_rave)


@router.message(Form.adding_score_gryf)
async def adding_score_gryf(message: Message, state: FSMContext):
    await message.answer(text=f"Баллы добавлены!", reply_markup=kb.make_row_keyboard(available_menus))
    with open('score.json', 'r', encoding='utf-8') as json_file:
        change_score = json.load(json_file)
    change_score["Гриффиндор"] += int(message.text)
    with open('score.json', 'w', encoding='utf-8') as json_file:
        json.dump(change_score, json_file, ensure_ascii=False, indent=4)
    await state.clear()


@router.message(Form.adding_score_slys)
async def adding_score_slys(message: Message, state: FSMContext):
    await message.answer(text=f"Баллы добавлены!", reply_markup=kb.make_row_keyboard(available_menus))
    with open('score.json', 'r', encoding='utf-8') as json_file:
        change_score = json.load(json_file)
    change_score["Слизерин"] += int(message.text)
    with open('score.json', 'w', encoding='utf-8') as json_file:
        json.dump(change_score, json_file, ensure_ascii=False, indent=4)
    await state.clear()


@router.message(Form.adding_score_huff)
async def adding_score_slys(message: Message, state: FSMContext):
    await message.answer(text=f"Баллы добавлены!", reply_markup=kb.make_row_keyboard(available_menus))
    with open('score.json', 'r', encoding='utf-8') as json_file:
        change_score = json.load(json_file)
    change_score["Хаффлпафф"] += int(message.text)
    with open('score.json', 'w', encoding='utf-8') as json_file:
        json.dump(change_score, json_file, ensure_ascii=False, indent=4)
    await state.clear()


@router.message(Form.adding_score_rave)
async def adding_score_slys(message: Message, state: FSMContext):
    await message.answer(text=f"Баллы добавлены!", reply_markup=kb.make_row_keyboard(available_menus))
    with open('score.json', 'r', encoding='utf-8') as json_file:
        change_score = json.load(json_file)
    change_score["Рейвенкло"] += int(message.text)
    with open('score.json', 'w', encoding='utf-8') as json_file:
        json.dump(change_score, json_file, ensure_ascii=False, indent=4)
    await state.clear()


@router.message(Form.choosing_facultet)
async def facultet_chosen_incorrectly(message: Message, state: FSMContext):
    await message.answer(
        text="Я не знаю такого факультета.\n\n"
             "Пожалуйста, выберите один из списка ниже:",
        reply_markup=kb.make_row_keyboard(available_facultets))
    await state.set_state(Form.choosing_facultet)


@router.message(Form.choosing_action)
async def action_chosen_incorrectly(message: Message, state: FSMContext):
    await message.answer(
        text="Я не знаю такого действия.\n\n"
             "Пожалуйста, выберите один из вариантов из списка ниже:",
        reply_markup=kb.make_row_keyboard(available_actions)
    )
    await state.set_state(Form.choosing_action)


'''
@router.callback_query(F.data == 'Добавить баллы')
async def Add_Score(callback: CallbackQuery):
    await callback.message.answer(f'Введите количество баллов')
    with open('score.json', 'r', encoding='utf-8') as json_file:
        change_score = json.load(json_file)
    with open('score.json', 'w', encoding='utf-8') as json_file:
        json.dump(change_score, json_file, ensure_ascii=False, indent=4)
'''


'''
@router.callback_query(F.data == 'Отнять баллы')
async def Add_Score(callback: CallbackQuery):
    await callback.message.answer(f'Введите количество баллов')

'''


@router.message()
async def echo(message: Message):
    await message.answer(f'Моя твоя не понимать, {message.from_user.first_name}',
                         reply_markup=kb.make_row_keyboard(available_menus))