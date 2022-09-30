from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers.start_menu import start
import crud
from db.main import get_db
from handlers import functions

db_generator = get_db()
db_session = next(db_generator)


discount = ['1', '2', '3', '5', '7', '10', 'Удалить покупателя']
buyer_end = ["Добавить покупателя", "В меню"]


async def buyer_start(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in buyer_end))
    await message.answer("Напишите имя покупателя", reply_markup=keyboard)
    await state.set_state("buyer_name_set")


async def buyer_name(message: types.Message, state: FSMContext):
    await state.update_data(buyer_name=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in buyer_end))
    await message.answer("Напишите фамилию покупателя", reply_markup=keyboard)
    await state.set_state("buyer_surname_set")


async def buyer_surname(message: types.Message, state: FSMContext):
    await state.update_data(buyer_surname=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in discount[:7]))
    keyboard.row(*(types.KeyboardButton(text) for text in discount[7:]))
    keyboard.row(*(types.KeyboardButton(text) for text in buyer_end))
    await message.answer("Выберите процент скидочной карты", reply_markup=keyboard)
    await state.set_state("buyer_discount_set")


async def buyer_discount(message: types.Message, state: FSMContext):
    if message.text not in discount:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(discount=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in buyer_end))
    await functions.buyer_add(message, state)
    await message.answer("Выберите действие:", reply_markup=keyboard)



def register_handlers_buyer(dp: Dispatcher):
    dp.register_message_handler(buyer_start, Text(equals="Добавить покупателя", ignore_case=True), state="*")
    dp.register_message_handler(start, Text(equals="В меню", ignore_case=True), state="*")

    dp.register_message_handler(buyer_name, state='buyer_name_set')
    dp.register_message_handler(buyer_surname, state='buyer_surname_set')
    dp.register_message_handler(buyer_discount, state='buyer_discount_set')


