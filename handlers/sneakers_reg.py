from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from handlers.start_menu import start
from db.main import get_db
from handlers import functions

db_generator = get_db()
db_session = next(db_generator)

sneakers_size = ["38", "39", "40", "41", "42", "43", "44"]
sneakers_type = ["Беговые", "Кеды", "Бутсы", "Баскетбольные", "Повседневные"]
sneakers_price = ['500', '1000', '1500', '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']
sneakers_colour = ["Черный", "Белый", "Синий", "Желтый", "Бордовый", "Розовый"]
sneakers_brand_name = ["Skechers", "Nike", "Adidas", "Reebok", "Demix"]
sneakers_num = ['1', '2', '3', '5', '10', '15', '20', '30', 'Убрать со склада']
sneakers_end = ["Добавить кроссовки", "В меню"]


async def sneakers_start(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in sneakers_type))
    keyboard.row(*(types.KeyboardButton(text) for text in sneakers_end))
    await message.answer("Выберите тип", reply_markup=keyboard)
    await state.set_state("sneakers_type_set")


async def type_sneakers(message: types.Message, state: FSMContext):
    if message.text not in sneakers_type:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(sneakers_type=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in sneakers_brand_name))
    keyboard.row(*(types.KeyboardButton(text) for text in sneakers_end))
    await message.answer("Выберите бренд", reply_markup=keyboard)
    await state.set_state("sneakers_brand_set")


async def brand_sneakers(message: types.Message, state: FSMContext):
    if message.text not in sneakers_brand_name:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(sneakers_brand_name=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in sneakers_size))
    keyboard.row(*(types.KeyboardButton(text) for text in sneakers_end))
    await message.answer("Выберите размер", reply_markup=keyboard)
    await state.set_state("sneakers_size_set")


async def size_sneakers(message: types.Message, state: FSMContext):
    if message.text not in sneakers_size:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(sneakers_size=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in sneakers_colour))
    keyboard.row(*(types.KeyboardButton(text) for text in sneakers_end))
    await message.answer("Выберите цвет", reply_markup=keyboard)
    await state.set_state("sneakers_colour_set")


async def colour_sneakers(message: types.Message, state: FSMContext):
    if message.text not in sneakers_colour:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(sneakers_colour=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in sneakers_price))
    keyboard.row(*(types.KeyboardButton(text) for text in sneakers_end))
    await message.answer("Выберите цену", reply_markup=keyboard)
    await state.set_state("sneakers_price_set")


async def price_sneakers(message: types.Message, state: FSMContext):
    if message.text not in sneakers_price:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(sneakers_price=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in sneakers_num))
    keyboard.row(*(types.KeyboardButton(text) for text in sneakers_end))
    await message.answer("Выберите количество или убрать товар со склада", reply_markup=keyboard)
    await state.set_state("sneakers_num_set")


async def num_sneakers(message: types.Message, state: FSMContext):
    if message.text not in sneakers_num:
        await message.answer("Пожалуйста, используйте клавиатуру ниже.")
        return
    await state.update_data(sneakers_num=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in sneakers_end))
    await functions.sneakers_add(message, state)
    await message.answer("Выберите действие:", reply_markup=keyboard)


def register_handlers_sneakers(dp: Dispatcher):
    dp.register_message_handler(sneakers_start, Text(equals="Добавить кроссовки", ignore_case=True), state="*")
    dp.register_message_handler(start, Text(equals="В меню", ignore_case=True), state="*")

    dp.register_message_handler(type_sneakers, state='sneakers_type_set')
    dp.register_message_handler(brand_sneakers, state='sneakers_brand_set')
    dp.register_message_handler(size_sneakers, state='sneakers_size_set')
    dp.register_message_handler(colour_sneakers, state='sneakers_colour_set')
    dp.register_message_handler(price_sneakers, state='sneakers_price_set')
    dp.register_message_handler(num_sneakers, state='sneakers_num_set')
