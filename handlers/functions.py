import crud
import schema
from db.main import get_db
import datetime

db_generator = get_db()
data_type = ['Пользователь', 'Группа', 'Назад', 'В меню']

"""Info_menu functions"""


async def pants_add(message, state):
    data = await state.get_data()
    db_session = next(db_generator)
    pants_size = data['pants_size'],
    pants_type = data['pants_type'],
    pants_price = data['pants_price'],
    pants_colour = data['pants_colour'],
    pants_in_stock = data['pants_num'],
    pants_brand_name = data['pants_brand_name']

    db_pants = crud.pants.check_five(db_session, "pants_size", pants_size,
                                     "pants_type", pants_type,
                                     "pants_price", pants_price,
                                     "pants_colour", pants_colour,
                                     "pants_brand_name", pants_brand_name)
    if db_pants:
        if pants_in_stock[0] == 'Убрать со склада':
            crud.pants.delete(db_session, "uid", db_pants.uid)
            await message.answer(f'Убраны со склада штаны:\n'
                                 f'{pants_type[0]}\n'
                                 f'{pants_brand_name}\n'
                                 f'Размер: {pants_size[0]}\n'
                                 f'Цвет: {pants_colour[0]}\n'
                                 f'Цена: {pants_price[0]}')
        else:
            num = db_pants.pants_in_stock + int(pants_in_stock[0])
            i = crud.pants.get(db_session, "uid", db_pants.uid)
            i.pants_in_stock = num
            db_session.add(i)
            db_session.commit()
            await message.answer(f'Количество товара увеличено на {pants_in_stock[0]}:\n'
                                 f'{pants_type[0]}\n'
                                 f'{pants_brand_name}\n'
                                 f'Размер: {pants_size[0]}\n'
                                 f'Цвет: {pants_colour[0]}\n'
                                 f'Цена: {pants_price[0]}\n'
                                 f'количество: {num}')

    if db_pants is None:
        new_pants = schema.pants.PantsCreate(
            pants_size=pants_size[0],
            pants_type=pants_type[0],
            pants_price=pants_price[0],
            pants_colour=pants_colour[0],
            pants_in_stock=int(pants_in_stock[0]),
            pants_brand_name=pants_brand_name
        )
        crud.pants.create(db_session, new_pants)
        await message.answer(f'Ассортимент расширен\nДобавлены штаны:\n'
                             f'{pants_type[0]}\n'
                             f'{pants_brand_name}\n'
                             f'Размер: {pants_size[0]}\n'
                             f'Цвет: {pants_colour[0]}\n'
                             f'Цена: {pants_price[0]}\n'
                             f'количество: {pants_in_stock[0]}')


async def sneakers_add(message, state):
    data = await state.get_data()
    db_session = next(db_generator)
    sneakers_size = data['sneakers_size'],
    sneakers_type = data['sneakers_type'],
    sneakers_price = data['sneakers_price'],
    sneakers_colour = data['sneakers_colour'],
    sneakers_in_stock = data['sneakers_num'],
    sneakers_brand_name = data['sneakers_brand_name']

    db_sneakers = crud.sneakers.check_five(db_session, "sneakers_size", sneakers_size,
                                           "sneakers_type", sneakers_type,
                                           "sneakers_price", sneakers_price,
                                           "sneakers_colour", sneakers_colour,
                                           "sneakers_brand_name", sneakers_brand_name)

    if db_sneakers:
        if sneakers_in_stock[0] == 'Убрать со склада':
            crud.sneakers.delete(db_session, "uid", db_sneakers.uid)
            await message.answer(f'Убраны со склада кроссовки:\n'
                                 f'{sneakers_type[0]}\n'
                                 f'{sneakers_brand_name}\n'
                                 f'Размер: {sneakers_size[0]}\n'
                                 f'Цвет: {sneakers_colour[0]}\n'
                                 f'Цена: {sneakers_price[0]}')
        else:
            num = db_sneakers.sneakers_in_stock + int(sneakers_in_stock[0])
            i = crud.sneakers.get(db_session, "uid", db_sneakers.uid)
            i.sneakers_in_stock = num
            db_session.add(i)
            db_session.commit()
            await message.answer(f'Количество товара увеличено на {sneakers_in_stock[0]}:\n'
                                 f'{sneakers_type[0]}\n'
                                 f'{sneakers_brand_name}\n'
                                 f'Размер: {sneakers_size[0]}\n'
                                 f'Цвет: {sneakers_colour[0]}\n'
                                 f'Цена: {sneakers_price[0]}\n'
                                 f'количество: {num}')

    if db_sneakers is None:
        new_sneakers = schema.sneakers.SneakersCreate(
            sneakers_size=sneakers_size[0],
            sneakers_type=sneakers_type[0],
            sneakers_price=sneakers_price[0],
            sneakers_colour=sneakers_colour[0],
            sneakers_in_stock=int(sneakers_in_stock[0]),
            sneakers_brand_name=sneakers_brand_name
        )
        crud.sneakers.create(db_session, new_sneakers)
        await message.answer(f'Ассортимент расширен\nДобавлены кроссовки:\n'
                             f'{sneakers_type[0]}\n'
                             f'{sneakers_brand_name}\n'
                             f'Размер: {sneakers_size[0]}\n'
                             f'Цвет: {sneakers_colour[0]}\n'
                             f'Цена: {sneakers_price[0]}\n'
                             f'количество: {sneakers_in_stock[0]}')


async def shirts_add(message, state):
    data = await state.get_data()
    db_session = next(db_generator)
    shirts_size = data['shirts_size'],
    shirts_type = data['shirts_type'],
    shirts_price = data['shirts_price'],
    shirts_colour = data['shirts_colour'],
    shirts_in_stock = data['shirts_num'],
    shirts_brand_name = data['shirts_brand_name']

    db_shirts = crud.shirts.check_five(db_session, "shirts_size", shirts_size,
                                       "shirts_type", shirts_type,
                                       "shirts_price", shirts_price,
                                       "shirts_colour", shirts_colour,
                                       "shirts_brand_name", shirts_brand_name)
    if db_shirts:
        if shirts_in_stock[0] == 'Убрать со склада':
            crud.shirts.delete(db_session, "uid", db_shirts.uid)
            await message.answer(f'Убраны со склада футболки:\n'
                                 f'{shirts_type[0]}\n'
                                 f'{shirts_brand_name}\n'
                                 f'Размер: {shirts_size[0]}\n'
                                 f'Цвет: {shirts_colour[0]}\n'
                                 f'Цена: {shirts_price[0]}')
        else:
            num = db_shirts.shirts_in_stock + int(shirts_in_stock[0])
            i = crud.shirts.get(db_session, "uid", db_shirts.uid)
            i.shirts_in_stock = num
            db_session.add(i)
            db_session.commit()
            await message.answer(f'Количество товара увеличено на {shirts_in_stock[0]}:\n'
                                 f'{shirts_type[0]}\n'
                                 f'{shirts_brand_name}\n'
                                 f'Размер: {shirts_size[0]}\n'
                                 f'Цвет: {shirts_colour[0]}\n'
                                 f'Цена: {shirts_price[0]}\n'
                                 f'количество: {num}')

    if db_shirts is None:
        new_shirts = schema.shirts.ShirtsCreate(
            shirts_size=shirts_size[0],
            shirts_type=shirts_type[0],
            shirts_price=shirts_price[0],
            shirts_colour=shirts_colour[0],
            shirts_in_stock=int(shirts_in_stock[0]),
            shirts_brand_name=shirts_brand_name
        )
        crud.shirts.create(db_session, new_shirts)
        await message.answer(f'Ассортимент расширен\nДобавлены футболки:\n'
                             f'{shirts_type[0]}\n'
                             f'{shirts_brand_name}\n'
                             f'Размер: {shirts_size[0]}\n'
                             f'Цвет: {shirts_colour[0]}\n'
                             f'Цена: {shirts_price[0]}\n'
                             f'количество: {shirts_in_stock[0]}')


async def buyer_add(message, state):
    data = await state.get_data()
    db_session = next(db_generator)
    name = data['buyer_name'],
    surname = data['buyer_surname'],
    discount = data['discount'],

    db_buyer = crud.buyer.check_two(db_session, "name", name, "surname", surname)

    if db_buyer:
        if discount[0] == 'Удалить покупателя':
            crud.buyer.delete(db_session, "uid", db_buyer.uid)
            await message.answer(f'Удалён покупатель:\n'
                                 f'{name[0]}\n'
                                 f'{surname[0]}')
        else:
            i = crud.buyer.get(db_session, "uid", db_buyer.uid)
            i.discount = discount[0]
            db_session.add(i)
            db_session.commit()
            await message.answer(f'Скидка для {surname[0]} {name[0]} изменена на {discount[0]}%')

    if db_buyer is None:
        new_buyer = schema.buyer.BuyerCreate(
            name=name[0],
            surname=surname[0],
            discount=int(discount[0])
        )
        crud.buyer.create(db_session, new_buyer)
        await message.answer(f'Добавлен покупатель {surname[0]} {name[0]} со скидочной картой на {discount[0]}%')


async def sum_buy(message, state, sneakers_buy, shirts_buy, pants_buy):
    data = await state.get_data()
    sum = data["buy_sum"]
    db_session = next(db_generator)
    if len(shirts_buy) != 0:
        for key, value in shirts_buy.items():
            shirts_db = crud.shirts.get(db_session, "uid", key)
            if value > shirts_db.shirts_in_stock:
                value = shirts_db.shirts_in_stock
            else:
                sum += shirts_db.shirts_price * value
    if len(sneakers_buy) != 0:
        for key, value in sneakers_buy.items():
            sneakers_db = crud.sneakers.get(db_session, "uid", key)
            if value > sneakers_db.sneakers_in_stock:
                value = sneakers_db.sneakers_in_stock
            else:
                sum += sneakers_db.sneakers_price * value
    if len(pants_buy) != 0:
        for key, value in pants_buy.items():
            pants_db = crud.pants.get(db_session, "uid", key)
            if value > pants_db.pants_in_stock:
                value = pants_db.pants_in_stock
            else:
                sum += pants_db.pants_price * value
    pants_buy.clear()
    sneakers_buy.clear()
    shirts_buy.clear()
    await state.update_data(buy_sum=sum)
    await message.answer(f"Сумма вашей корзины = {sum}")


async def create_check(message, state, sneakers_check, shirts_check, pants_check, user):
    data = await state.get_data()
    sum = data["buy_sum"]
    db_session = next(db_generator)
    db_buyer = crud.buyer.get(db_session, "surname", user)
    sum = sum * (1 - db_buyer.discount * 0.01)
    new_check = schema.check.CheckCreate(
        buyer_uid=db_buyer.uid,
        check_sum=sum
    )
    db = crud.check.create(db_session, new_check)
    date_now = datetime.datetime.today()
    db.date = date_now
    db_session.add(db)
    db_session.commit()
    db_check = crud.check.get(db_session, "uid", db.uid)
    if len(shirts_check) != 0:
        for key, value in shirts_check.items():
            buy_sum = 0
            shirts_db = crud.shirts.get(db_session, "uid", key)
            if value > shirts_db.shirts_in_stock:
                value = shirts_db.shirts_in_stock
            else:
                buy_sum += shirts_db.shirts_price * value
                new_buy = schema.buy.BuyCreate(
                    check_uid=db_check.uid,
                    shirts_uid=shirts_db.uid,
                    shirts_num=value,
                    sneakers_uid=0,
                    sneakers_num=0,
                    pants_uid=0,
                    pants_num=0,
                    buy_sum=buy_sum
                )
                crud.buy.create(db_session, new_buy)
                num = shirts_db.shirts_in_stock - value
                shirts_db.shirts_in_stock = num
                db_session.add(shirts_db)
                db_session.commit()

    if len(sneakers_check) != 0:
        for key, value in sneakers_check.items():
            buy_sum = 0
            sneakers_db = crud.sneakers.get(db_session, "uid", key)
            if value > sneakers_db.sneakers_in_stock:
                value = sneakers_db.sneakers_in_stock
            else:
                buy_sum += sneakers_db.sneakers_price * value
                new_buy = schema.buy.BuyCreate(
                    check_uid=db_check.uid,
                    sneakers_uid=sneakers_db.uid,
                    sneakers_num=value,
                    pants_uid=0,
                    pants_num=0,
                    shirts_uid=0,
                    shirts_num=0,
                    buy_sum=buy_sum
                )
                crud.buy.create(db_session, new_buy)
                num = sneakers_db.sneakers_in_stock - value
                sneakers_db.sneakers_in_stock = num
                db_session.add(sneakers_db)
                db_session.commit()

    if len(pants_check) != 0:
        for key, value in shirts_check.items():
            buy_sum = 0
            pants_db = crud.pants.get(db_session, "uid", key)
            if value > pants_db.pants_in_stock:
                value = pants_db.pants_in_stock
            else:
                buy_sum += pants_db.pants_price * value
                new_buy = schema.buy.BuyCreate(
                    check_uid=db_check.uid,
                    pants_uid=pants_db.uid,
                    pants_num=value,
                    sneakers_uid=0,
                    sneakers_num=0,
                    shirts_uid=0,
                    shirts_num=0,
                    buy_sum=buy_sum
                )
                crud.buy.create(db_session, new_buy)
                num = pants_db.pants_in_stock - value
                pants_db.pants_in_stock = num
                db_session.add(pants_db)
                db_session.commit()
    await message.answer('Спасибо за покупку!')
