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


shirts_size = ["XS", "S", "M", "L", "XL", "XXL"]
shirts_type = ["С длинным рукавом", "С коротким рукавом", "Джерси", "Поло"]
shirts_price = ['500', '1000', '1500', '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']
shirts_colour = ["Черный", "Белый", "Синий", "Желтый", "Бордовый", "Розовый"]
shirts_brand_name = ["Skechers", "Nike", "Adidas", "Reebok", "Demix"]
shirts_num = ['1', '2', '3', '5', '10', '15', '20', '30', 'Убрать со склада']
shirts_end = ["Добавить футболки", "В меню"]


async def shirts_start(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in shirts_type))
    keyboard.row(*(types.KeyboardButton(text) for text in shirts_end))
    await message.answer("Выберите тип", reply_markup=keyboard)
    await state.set_state("shirts_type_set")


async def type_shirts(message: types.Message, state: FSMContext):
    if message.text not in shirts_type:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(shirts_type=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in shirts_brand_name))
    keyboard.row(*(types.KeyboardButton(text) for text in shirts_end))
    await message.answer("Выберите бренд", reply_markup=keyboard)
    await state.set_state("shirts_brand_set")


async def brand_shirts(message: types.Message, state: FSMContext):
    if message.text not in shirts_brand_name:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(shirts_brand_name=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in shirts_size))
    keyboard.row(*(types.KeyboardButton(text) for text in shirts_end))
    await message.answer("Выберите размер", reply_markup=keyboard)
    await state.set_state("shirts_size_set")


async def size_shirts(message: types.Message, state: FSMContext):
    if message.text not in shirts_size:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(shirts_size=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in shirts_colour))
    keyboard.row(*(types.KeyboardButton(text) for text in shirts_end))
    await message.answer("Выберите цвет", reply_markup=keyboard)
    await state.set_state("shirts_colour_set")


async def colour_shirts(message: types.Message, state: FSMContext):
    if message.text not in shirts_colour:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(shirts_colour=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in shirts_price))
    keyboard.row(*(types.KeyboardButton(text) for text in shirts_end))
    await message.answer("Выберите цену", reply_markup=keyboard)
    await state.set_state("shirts_price_set")


async def price_shirts(message: types.Message, state: FSMContext):
    if message.text not in shirts_price:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(shirts_price=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in shirts_num))
    keyboard.row(*(types.KeyboardButton(text) for text in shirts_end))
    await message.answer("Выберите количество или убрать товар со склада", reply_markup=keyboard)
    await state.set_state("shirts_num_set")


async def num_shirts(message: types.Message, state: FSMContext):
    if message.text not in shirts_num:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(shirts_num=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in shirts_end))
    await functions.shirts_add(message, state)
    await message.answer("Выберите действие:", reply_markup=keyboard)


def register_handlers_shirts(dp: Dispatcher):
    dp.register_message_handler(shirts_start, Text(equals="Добавить футболки", ignore_case=True), state="*")
    dp.register_message_handler(start, Text(equals="В меню", ignore_case=True), state="*")

    dp.register_message_handler(type_shirts, state='shirts_type_set')
    dp.register_message_handler(brand_shirts, state='shirts_brand_set')
    dp.register_message_handler(size_shirts, state='shirts_size_set')
    dp.register_message_handler(colour_shirts, state='shirts_colour_set')
    dp.register_message_handler(price_shirts, state='shirts_price_set')
    dp.register_message_handler(num_shirts, state='shirts_num_set')

