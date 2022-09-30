from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers.start_menu import start, all_buyers

import crud
from db.main import get_db
from handlers import functions

db_generator = get_db()
db_session = next(db_generator)
shirts_types = ["С длинным рукавом", "С коротким рукавом", "Джерси", "Поло"]
pants_types = ["Шорты", "Брюки", "Джоггеры", "Термо"]
sneakers_types = ["Беговые", "Кеды", "Бутсы", "Баскетбольные", "Повседневные"]

start_buy = ['Выбрать футболку', 'Выбрать штаны', 'Выбрать кроссовки', 'Совершить покупку']
buy_end = ["Купить", "В меню"]
pants_buy = {}
shirts_buy = {}
sneakers_buy = {}
pants_check = {}
shirts_check = {}
sneakers_check = {}

async def buy_start(message: types.Message, state: FSMContext):
    await state.update_data(buy_sum=0)
    sneakers_check.clear()
    shirts_check.clear()
    pants_check.clear()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in start_buy))
    keyboard.row(*(types.KeyboardButton(text) for text in buy_end))
    await state.set_state("buy_start_set")
    await message.answer("Наберите корзину и совершите покупку", reply_markup=keyboard)


async def buy_type(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    data = await state.get_data()
    sum = data["buy_sum"]
    if message.text not in start_buy:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    if message.text == 'Выбрать футболку':
        keyboard.row(*(types.KeyboardButton(text) for text in shirts_types))
    if message.text == 'Выбрать штаны':
        keyboard.row(*(types.KeyboardButton(text) for text in pants_types))
    if message.text == 'Выбрать кроссовки':
        keyboard.row(*(types.KeyboardButton(text) for text in sneakers_types))
    if message.text == 'Совершить покупку':
        if sum < 0:
            keyboard.row(*(types.KeyboardButton(text) for text in start_buy))
            keyboard.row(*(types.KeyboardButton(text) for text in buy_end))
            await message.answer("Вы не выбрали товар", reply_markup=keyboard)
            return
        for value in all_buyers:
            keyboard.add(value)
        keyboard.row(*(types.KeyboardButton(text) for text in start_buy))
        keyboard.row(*(types.KeyboardButton(text) for text in buy_end))
        await message.answer("Представьтесь", reply_markup=keyboard)
        await state.set_state("close_buy_set")
        return
    keyboard.row(*(types.KeyboardButton(text) for text in start_buy))
    keyboard.row(*(types.KeyboardButton(text) for text in buy_end))
    await message.answer("Выберите тип", reply_markup=keyboard)
    await state.set_state("wait_buy_set")


async def wait_buy(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text in shirts_types:
        await state.update_data(buy_set='shirts')
        show_shirts = iter(crud.shirts.get_all_field_by_one(db_session, 'shirts_type', message.text, 'shirts_size'))
        text = ''
        for records in show_shirts:
            text += f"{records.uid}. {records.shirts_brand_name} {records.shirts_colour} " \
                    f"размер: {records.shirts_size} Цена {records.shirts_price}р" \
                    f" в наличии: {records.shirts_in_stock}\n"
        await message.answer(f"Ассортимент {message.text}:\n{text}", reply_markup=keyboard)
        await message.answer("Напишите необходимый код товара и :количество\n"
                             "В формате 14:3, 11:2")
        await state.set_state("buy_end_set")
        return
    if message.text in pants_types:
        await state.update_data(buy_set='pants')
        show_pants = iter(crud.pants.get_all_field_by_one(db_session, 'pants_type', message.text, 'pants_size'))
        text = ''
        for records in show_pants:
            text += f"{records.uid}. {records.pants_brand_name} {records.pants_colour} " \
                    f"размер: {records.pants_size} Цена {records.pants_price}р" \
                    f" в наличии: {records.pants_in_stock}\n"
        await message.answer(f"Ассортимент {message.text}:\n{text}", reply_markup=keyboard)
        await message.answer("Напишите необходимый код товара и :количество\n"
                             "В формате 14:3, 11:2")
        await state.set_state("buy_end_set")
        return
    if message.text in sneakers_types:
        await state.update_data(buy_set='sneakers')
        show_sneakers = iter(crud.sneakers.get_all_field_by_one(db_session, 'sneakers_type',
                                                                message.text, 'sneakers_size'))
        text = ''
        for records in show_sneakers:
            text += f"{records.uid}. {records.sneakers_brand_name} {records.sneakers_colour} " \
                    f"размер: {records.sneakers_size} Цена {records.sneakers_price}р" \
                    f" в наличии: {records.sneakers_in_stock}\n"
        await message.answer(f"Ассортимент {message.text}:\n{text}", reply_markup=keyboard)
        await message.answer("Напишите необходимый код товара и :количество\n"
                             "В формате 14:3, 11:2")
        await state.set_state("buy_end_set")
        return
    if message.text not in (sneakers_types and shirts_types and pants_types):
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return


async def end_buy(message: types.Message, state: FSMContext):
    data = await state.get_data()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    uid_data = [item.split(':') for item in message.text.split(',')]
    if data['buy_set'] == 'sneakers':
        for i in uid_data:
            sneakers_buy[int(i[0])] = int(i[1])
            sneakers_check[int(i[0])] = int(i[1])
    if data['buy_set'] == 'pants':
        for i in uid_data:
            pants_buy[int(i[0])] = int(i[1])
            pants_check[int(i[0])] = int(i[1])
    if data['buy_set'] == 'shirts':
        for i in uid_data:
            shirts_buy[int(i[0])] = int(i[1])
            shirts_check[int(i[0])] = int(i[1])
    keyboard.row(*(types.KeyboardButton(text) for text in start_buy))
    keyboard.row(*(types.KeyboardButton(text) for text in buy_end))
    await message.answer("Товар добавлен в корзину")
    await functions.sum_buy(message, state, sneakers_buy, shirts_buy, pants_buy)
    await message.answer("Наберите корзину и совершите покупку", reply_markup=keyboard)
    await state.set_state("buy_start_set")

async def close_buy(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text not in all_buyers:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    user = message.text
    data = await state.get_data()
    sum = data["buy_sum"]
    keyboard.row(*(types.KeyboardButton(text) for text in buy_end))
    db_buyer = crud.buyer.get(db_session, "surname", user)
    sum = sum * (1 - db_buyer.discount*0.01)
    await message.answer(f"Здравствуйте, {db_buyer.name} {db_buyer.surname}\n"
                         f"С учетом скидки в {db_buyer.discount}% сумма вашей покупки: {int(sum)}",
                         reply_markup=keyboard)
    await functions.create_check(message, state, sneakers_check, shirts_check, pants_check, user)


def register_handlers_buy(dp: Dispatcher):
    dp.register_message_handler(buy_start, Text(equals="Купить", ignore_case=True), state="*")
    dp.register_message_handler(start, Text(equals="В меню", ignore_case=True), state="*")
    dp.register_message_handler(buy_type, state="buy_start_set")
    dp.register_message_handler(wait_buy, state="wait_buy_set")
    dp.register_message_handler(end_buy, state="buy_end_set")
    dp.register_message_handler(close_buy, state="close_buy_set")

    dp.register_message_handler(start, Text(equals='Совершить покупку'), state="*")
