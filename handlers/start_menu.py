from aiogram import types
from aiogram import Dispatcher
import crud
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from db.main import get_db

db_generator = get_db()
db_session = next(db_generator)

class OrderStart(StatesGroup):
    start_set = State()

all_buyers = []
buyers = iter(crud.buyer.get_all_field(db_session, 'surname'))
if buyers:
    for records in buyers:
        all_buyers.append(records.surname)
start_menu = ["Добавить штаны", "Добавить кроссовки", "Добавить футболки", "Добавить покупателя", "Купить"]


async def start(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=False)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*(types.KeyboardButton(text) for text in start_menu[:4]))
    keyboard.add("Купить")
    await message.answer("Выберите действие:", reply_markup=keyboard)


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_message_handler(start, lambda msg: msg.text.lower() == 'отмена', state="*")
