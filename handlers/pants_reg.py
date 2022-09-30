from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from handlers.start_menu import start
from db.main import get_db
from handlers import functions

db_generator = get_db()
db_session = next(db_generator)


pants_size = ["XS", "S", "M", "L", "XL", "XXL"]
pants_type = ["Шорты", "Брюки", "Джоггеры", "Термо"]
pants_price = ['500', '1000', '1500', '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']
pants_colour = ["Черный", "Белый", "Синий", "Желтый", "Бордовый", "Розовый"]
pants_brand_name = ["Skechers", "Nike", "Adidas", "Reebok", "Demix"]
pants_num = ['1', '2', '5', '10', '15', '20', '30', '50', '100', 'Убрать со склада']
pants_end = ["Добавить штаны", "В меню"]


async def pants_start(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in pants_type))
    keyboard.row(*(types.KeyboardButton(text) for text in pants_end))
    await message.answer("Выберите тип", reply_markup=keyboard)
    await state.set_state("pants_type_set")


async def type_pants(message: types.Message, state: FSMContext):
    if message.text not in pants_type:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(pants_type=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in pants_brand_name))
    keyboard.row(*(types.KeyboardButton(text) for text in pants_end))
    await message.answer("Выберите бренд", reply_markup=keyboard)
    await state.set_state("pants_brand_set")


async def brand_pants(message: types.Message, state: FSMContext):
    if message.text not in pants_brand_name:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(pants_brand_name=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in pants_size))
    keyboard.row(*(types.KeyboardButton(text) for text in pants_end))
    await message.answer("Выберите размер", reply_markup=keyboard)
    await state.set_state("pants_size_set")


async def size_pants(message: types.Message, state: FSMContext):
    if message.text not in pants_size:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(pants_size=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in pants_colour))
    keyboard.row(*(types.KeyboardButton(text) for text in pants_end))
    await message.answer("Выберите цвет", reply_markup=keyboard)
    await state.set_state("pants_colour_set")


async def colour_pants(message: types.Message, state: FSMContext):
    if message.text not in pants_colour:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(pants_colour=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in pants_price))
    keyboard.row(*(types.KeyboardButton(text) for text in pants_end))
    await message.answer("Выберите цену", reply_markup=keyboard)
    await state.set_state("pants_price_set")


async def price_pants(message: types.Message, state: FSMContext):
    if message.text not in pants_price:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(pants_price=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in pants_num))
    keyboard.row(*(types.KeyboardButton(text) for text in pants_end))
    await message.answer("Выберите количество или убрать товар со склада", reply_markup=keyboard)
    await state.set_state("pants_num_set")


async def num_pants(message: types.Message, state: FSMContext):
    if message.text not in pants_num:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(pants_num=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in pants_end))
    await functions.pants_add(message, state)
    await message.answer("Выберите действие:", reply_markup=keyboard)


def register_handlers_pants(dp: Dispatcher):
    dp.register_message_handler(pants_start, Text(equals="Добавить штаны", ignore_case=True), state="*")
    dp.register_message_handler(start, Text(equals="В меню", ignore_case=True), state="*")

    dp.register_message_handler(type_pants, state='pants_type_set')
    dp.register_message_handler(brand_pants, state='pants_brand_set')
    dp.register_message_handler(size_pants, state='pants_size_set')
    dp.register_message_handler(colour_pants, state='pants_colour_set')
    dp.register_message_handler(price_pants, state='pants_price_set')
    dp.register_message_handler(num_pants, state='pants_num_set')

