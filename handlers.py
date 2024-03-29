from aiogram import Router, Bot, F
from aiogram.types import Message, FSInputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from settings import settings
import keyboards as kb
import json

storage = MemoryStorage()
router = Router()
router.message.filter(F.chat.type == "private")
bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

available_facultets = ["Гриффиндор", "Слизерин", "Хаффлпафф", "Рейвенкло"]
available_actions = ["Добавить баллы", "Вычесть баллы"]
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
    removing_score_gryf = State()
    removing_score_slys = State()
    removing_score_huff = State()
    removing_score_rave = State()
    score_info = State()


class AwaitMessages(StatesGroup):
    fio_add = State()


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer(text="Добро пожаловать, введите должность и ФИО")
    await state.set_state(AwaitMessages.fio_add)


@router.message(AwaitMessages.fio_add)
async def process_fio_add(message: Message, state: FSMContext):
    with open('FIO.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        while True:
            key = message.from_user.first_name
            value = message.text
            data[key] = value
            break
    with open('FIO.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    await message.answer(text=f'Приветствую, {message.text}. Выберите пункт меню',
                         reply_markup=kb.make_row_keyboard(available_menus))
    await message.answer(text=f'Либо введите команду /log для просмотра истории')
    await state.set_state(Form.start)


@router.message(Form.start, F.text == "Узнать количество баллов")
async def get_score_info(message: Message, state: FSMContext):
    await message.answer(text="Текущее количество баллов у факультетов:",
                         reply_markup=kb.make_row_keyboard(available_menus))
    with open('score.json', 'r', encoding='utf-8') as json_file:
        score_dict = json.load(json_file)
        s = json.dumps(score_dict, skipkeys=False, ensure_ascii=False, indent=0, sort_keys=False)
        result = s.strip("{}")
        result = result.replace(",", "").replace('"', '')
        await message.answer(result)
    await state.set_state(Form.start)


@router.message(Form.start, F.text == "Выбрать факультет")
async def menu_chosen(message: Message, state: FSMContext):
    await message.answer(
        text="Спасибо. Теперь, пожалуйста, выберите факультет",
        reply_markup=kb.make_row_keyboard(available_facultets)
    )
    await state.set_state(Form.choosing_facultet)


@router.message(Form.choosing_facultet, F.text == "Гриффиндор")
async def facultet_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали факультет {message.text.lower()}.\n"
             f"Теперь выберите действие:",
        reply_markup=kb.make_row_keyboard(available_actions))
    await state.set_state(Form.choosing_action_gryf)


@router.message(Form.choosing_facultet, F.text == "Слизерин")
async def facultet_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали факультет {message.text.lower()}.\n"
             f"Теперь выберите действие:",
        reply_markup=kb.make_row_keyboard(available_actions))
    await state.set_state(Form.choosing_action_slys)


@router.message(Form.choosing_facultet, F.text == "Хаффлпафф")
async def facultet_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали факультет {message.text.lower()}.\n"
             f"Теперь выберите действие:",
        reply_markup=kb.make_row_keyboard(available_actions))
    await state.set_state(Form.choosing_action_huff)


@router.message(Form.choosing_facultet, F.text == "Рейвенкло")
async def facultet_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали факультет {message.text.lower()}.\n"
             f"Теперь выберите действие:",
        reply_markup=kb.make_row_keyboard(available_actions))
    await state.set_state(Form.choosing_action_rave)


@router.message(Form.choosing_action_gryf, F.text == "Добавить баллы")
async def action_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} факультету.\n\n Введите количество баллов",
        reply_markup=kb.make_row_keyboard(available_menus)
    )
    await state.set_state(Form.adding_score_gryf)


@router.message(Form.choosing_action_slys, F.text == "Добавить баллы")
async def action_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} факультету.\n\n Введите количество баллов",
        reply_markup=kb.make_row_keyboard(available_menus)
    )
    await state.set_state(Form.adding_score_slys)


@router.message(Form.choosing_action_huff, F.text == "Добавить баллы")
async def action_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} факультету.\n\n Введите количество баллов",
        reply_markup=kb.make_row_keyboard(available_menus)
    )
    await state.set_state(Form.adding_score_huff)


@router.message(Form.choosing_action_rave, F.text == "Добавить баллы")
async def action_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} факультету.\n\n Введите количество баллов",
        reply_markup=kb.make_row_keyboard(available_menus)
    )
    await state.set_state(Form.adding_score_rave)


@router.message(Form.choosing_action_gryf, F.text == "Вычесть баллы")
async def action_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} факультету.\n\n Введите количество баллов",
        reply_markup=kb.make_row_keyboard(available_menus)
    )
    await state.set_state(Form.removing_score_gryf)


@router.message(Form.choosing_action_slys, F.text == "Вычесть баллы")
async def action_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} факультету.\n\n Введите количество баллов",
        reply_markup=kb.make_row_keyboard(available_menus)
    )
    await state.set_state(Form.removing_score_slys)


@router.message(Form.choosing_action_huff, F.text == "Вычесть баллы")
async def action_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} факультету.\n\n Введите количество баллов",
        reply_markup=kb.make_row_keyboard(available_menus)
    )
    await state.set_state(Form.removing_score_huff)


@router.message(Form.choosing_action_rave, F.text == "Вычесть баллы")
async def action_chosen(message: Message, state: FSMContext):
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} факультету.\n\n Введите количество баллов",
        reply_markup=kb.make_row_keyboard(available_menus)
    )
    await state.set_state(Form.removing_score_rave)


@router.message(Form.adding_score_gryf)
async def adding_score_gryf(message: Message, state: FSMContext):
    a = message.text
    if a.isdigit():
        await message.answer(text=f"Баллы добавлены!", reply_markup=kb.make_row_keyboard(available_menus))
        with open('score.json', 'r', encoding='utf-8') as json_file:
            change_score = json.load(json_file)
        change_score["Гриффиндор"] += int(a)
        with open('score.json', 'w', encoding='utf-8') as json_file:
            json.dump(change_score, json_file, ensure_ascii=False, indent=4)
        with open('FIO.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            key = message.from_user.first_name
        x = (data[key], "добавил(а)", int(a), "баллов Гриффиндору")
        with open('log.txt', 'a') as f:
            print(str(x)[1:-1].replace("'", "").replace(",", ""), file=f)
        await state.set_state(Form.start)
    else:
        await message.answer(text="Это не число, попробуйте ещё раз")


@router.message(Form.adding_score_slys)
async def adding_score_slys(message: Message, state: FSMContext):
    a = message.text
    if a.isdigit():
        await message.answer(text=f"Баллы добавлены!", reply_markup=kb.make_row_keyboard(available_menus))
        with open('score.json', 'r', encoding='utf-8') as json_file:
            change_score = json.load(json_file)
        change_score["Слизерин"] += int(a)
        with open('score.json', 'w', encoding='utf-8') as json_file:
            json.dump(change_score, json_file, ensure_ascii=False, indent=4)
        with open('FIO.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            key = message.from_user.first_name
        x = (data[key], 'добавил(а)', int(a), 'баллов Слизерину')
        with open('log.txt', 'a') as f:
            print(str(x)[1:-1].replace("'", "").replace(",", ""), file=f)
        await state.set_state(Form.start)
    else:
        await message.answer(text="Это не число, попробуйте ещё раз")


@router.message(Form.adding_score_huff)
async def adding_score_huff(message: Message, state: FSMContext):
    a = message.text
    if a.isdigit():
        await message.answer(text=f"Баллы добавлены!", reply_markup=kb.make_row_keyboard(available_menus))
        with open('score.json', 'r', encoding='utf-8') as json_file:
            change_score = json.load(json_file)
        change_score["Хаффлпафф"] += int(a)
        with open('score.json', 'w', encoding='utf-8') as json_file:
            json.dump(change_score, json_file, ensure_ascii=False, indent=4)
        with open('FIO.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            key = message.from_user.first_name
        x = (data[key], "добавил(а)", int(a), "баллов Хаффлпаффу")
        with open('log.txt', 'a') as f:
            print(str(x)[1:-1].replace("'", "").replace(",", ""), file=f)
        await state.set_state(Form.start)
    else:
        await message.answer(text="Это не число, попробуйте ещё раз")


@router.message(Form.adding_score_rave)
async def adding_score_rave(message: Message, state: FSMContext):
    a = message.text
    if a.isdigit():
        await message.answer(text=f"Баллы добавлены!", reply_markup=kb.make_row_keyboard(available_menus))
        with open('score.json', 'r', encoding='utf-8') as json_file:
            change_score = json.load(json_file)
        change_score["Рейвенкло"] += int(a)
        with open('score.json', 'w', encoding='utf-8') as json_file:
            json.dump(change_score, json_file, ensure_ascii=False, indent=4)
        with open('FIO.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            key = message.from_user.first_name
        x = (data[key], "добавил(а)", int(a), "баллов Рейвенкло")
        with open('log.txt', 'a') as f:
            print(str(x)[1:-1].replace("'", "").replace(",", ""), file=f)
        await state.set_state(Form.start)
    else:
        await message.answer(text="Это не число, попробуйте ещё раз")


@router.message(Form.removing_score_gryf)
async def removing_score_gryf(message: Message, state: FSMContext):
    a = message.text
    if a.isdigit():
        await message.answer(text=f"Баллы вычтены!", reply_markup=kb.make_row_keyboard(available_menus))
        with open('score.json', 'r', encoding='utf-8') as json_file:
            change_score = json.load(json_file)
            change_score["Гриффиндор"] -= int(a)
        if int(a) > change_score["Гриффиндор"]:
            change_score["Гриффиндор"] = 0
            await message.answer(text="Количество баллов не может быть меньше нуля.")
            await message.answer(text="Теперь у Гриффиндора 0 баллов.")
            with open('score.json', 'w', encoding='utf-8') as json_file:
                json.dump(change_score, json_file, ensure_ascii=False, indent=4)
            with open('FIO.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                key = message.from_user.first_name
            x = (data[key], "попробовал(а) вычесть", int(a), "баллов у Гриффиндора и теперь количество баллов = 0")
            with open('log.txt', 'a') as f:
                print(str(x)[1:-1].replace("'", "").replace(",", ""), file=f)
            await state.set_state(Form.start)
        else:
            with open('score.json', 'w', encoding='utf-8') as json_file:
                json.dump(change_score, json_file, ensure_ascii=False, indent=4)
            with open('FIO.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                key = message.from_user.first_name
            x = (data[key], "вычел(чла)", int(a), "баллов у Гриффиндора")
            with open('log.txt', 'a') as f:
                print(str(x)[1:-1].replace("'", "").replace(",", ""), file=f)
        await state.set_state(Form.start)
    else:
        await message.answer(text="Это не число, попробуйте ещё раз")


@router.message(Form.removing_score_slys)
async def removing_score_slys(message: Message, state: FSMContext):
    a = message.text
    if a.isdigit():
        await message.answer(text=f"Баллы вычтены!", reply_markup=kb.make_row_keyboard(available_menus))
        with open('score.json', 'r', encoding='utf-8') as json_file:
            change_score = json.load(json_file)
            change_score["Слизерин"] -= int(a)
        if int(a) > change_score["Слизерин"]:
            change_score["Слизерин"] = 0
            await message.answer(text="Количество баллов не может быть меньше нуля.")
            await message.answer(text="Теперь у Слизерина 0 баллов.")
            with open('score.json', 'w', encoding='utf-8') as json_file:
                json.dump(change_score, json_file, ensure_ascii=False, indent=4)
            with open('FIO.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                key = message.from_user.first_name
            x = (data[key], "попробовал(а) вычесть", int(a), "баллов у Слизерина и теперь количество баллов = 0")
            with open('log.txt', 'a') as f:
                print(str(x)[1:-1].replace("'", "").replace(",", ""), file=f)
            await state.set_state(Form.start)
        else:
            with open('score.json', 'w', encoding='utf-8') as json_file:
                json.dump(change_score, json_file, ensure_ascii=False, indent=4)
            with open('FIO.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                key = message.from_user.first_name
            x = (data[key], "вычел(чла)", int(a), "баллов у Слизерина")
            with open('log.txt', 'a') as f:
                print(str(x)[1:-1].replace("'", "").replace(",", ""), file=f)
        await state.set_state(Form.start)
    else:
        await message.answer(text="Это не число, попробуйте ещё раз")


@router.message(Form.removing_score_huff)
async def removing_score_huff(message: Message, state: FSMContext):
    a = message.text
    if a.isdigit():
        await message.answer(text=f"Баллы вычтены!", reply_markup=kb.make_row_keyboard(available_menus))
        with open('score.json', 'r', encoding='utf-8') as json_file:
            change_score = json.load(json_file)
            change_score["Хаффлпафф"] -= int(a)
        if int(a) > change_score["Хаффлпафф"]:
            change_score["Хаффлпафф"] = 0
            await message.answer(text="Количество баллов не может быть меньше нуля.")
            await message.answer(text="Теперь у Хаффлпаффа 0 баллов.")
            with open('score.json', 'w', encoding='utf-8') as json_file:
                json.dump(change_score, json_file, ensure_ascii=False, indent=4)
            with open('FIO.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                key = message.from_user.first_name
            x = (data[key], "попробовал(а) вычесть", int(a), "баллов у Хаффлпаффа и теперь количество баллов = 0")
            with open('log.txt', 'a') as f:
                print(str(x)[1:-1].replace("'", "").replace(",", ""), file=f)
            await state.set_state(Form.start)
        else:
            with open('score.json', 'w', encoding='utf-8') as json_file:
                json.dump(change_score, json_file, ensure_ascii=False, indent=4)
            with open('FIO.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                key = message.from_user.first_name
            x = (data[key], "вычел(чла)", int(a), "баллов у Хаффлпаффа")
            with open('log.txt', 'a') as f:
                print(str(x)[1:-1].replace("'", "").replace(",", ""), file=f)
        await state.set_state(Form.start)
    else:
        await message.answer(text="Это не число, попробуйте ещё раз")


@router.message(Form.removing_score_rave)
async def removing_score_rave(message: Message, state: FSMContext):
    a = message.text
    if a.isdigit():
        await message.answer(text=f"Баллы вычтены!", reply_markup=kb.make_row_keyboard(available_menus))
        with open('score.json', 'r', encoding='utf-8') as json_file:
            change_score = json.load(json_file)
            change_score["Рейвенкло"] -= int(a)
        if int(a) > change_score["Рейвенкло"]:
            change_score["Рейвенкло"] = 0
            await message.answer(text="Количество баллов не может быть меньше нуля.")
            await message.answer(text="Теперь у Рейвенкло 0 баллов.")
            with open('score.json', 'w', encoding='utf-8') as json_file:
                json.dump(change_score, json_file, ensure_ascii=False, indent=4)
            with open('FIO.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                key = message.from_user.first_name
            x = (data[key], "попробовал(а) вычесть", int(a), "баллов у Рейвенкло и теперь количество баллов = 0")
            with open('log.txt', 'a') as f:
                print(str(x)[1:-1].replace("'", "").replace(",", ""), file=f)
            await state.set_state(Form.start)
        else:
            with open('score.json', 'w', encoding='utf-8') as json_file:
                json.dump(change_score, json_file, ensure_ascii=False, indent=4)
            with open('FIO.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                key = message.from_user.first_name
            x = (data[key], "вычел(чла)", int(a), "баллов у Рейвенкло")
            with open('log.txt', 'a') as f:
                print(str(x)[1:-1].replace("'", "").replace(",", ""), file=f)
        await state.set_state(Form.start)
    else:
        await message.answer(text="Это не число, попробуйте ещё раз")


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


@router.message(Command("log"))
async def log_download(message: Message):
    doc = FSInputFile('log.txt')
    usr_id = message.from_user.id
    await bot.send_document(document=doc, chat_id=usr_id)


@router.message()
async def echo(message: Message, state: FSMContext):
    await message.answer(f'Моя твоя не понимать, {message.from_user.first_name}',
                         reply_markup=kb.make_row_keyboard(available_menus))
    await state.set_state(Form.start)
