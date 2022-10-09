from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func
from db.main import Base
import datetime


class Shirts(Base):
    __tablename__ = "Футболки"

    uid = Column(Integer, autoincrement=True, primary_key=True, index=True)
    shirts_type = Column(Text)
    shirts_brand_name = Column(Text)
    shirts_size = Column(Text)
    shirts_colour = Column(Text)
    shirts_price = Column(Integer)
    shirts_in_stock = Column(Integer)


class Pants(Base):
    __tablename__ = "Штаны"

    uid = Column(Integer, autoincrement=True, primary_key=True, index=True)
    pants_type = Column(Text)
    pants_brand_name = Column(Text)
    pants_size = Column(Text)
    pants_colour = Column(Text)
    pants_price = Column(Integer)
    pants_in_stock = Column(Integer)


    # region = relationship("Region", back_populates="sources")


class Sneakers(Base):
    __tablename__ = "Кроссовки"

    uid = Column(Integer, autoincrement=True, primary_key=True, index=True)
    sneakers_type = Column(Text)
    sneakers_brand_name = Column(Text)
    sneakers_size = Column(Text)
    sneakers_colour = Column(Text)
    sneakers_price = Column(Integer)
    sneakers_in_stock = Column(Integer)


class Buy(Base):
    __tablename__ = "Покупка"

    uid = Column(Integer, autoincrement=True, primary_key=True, index=True)
    check_uid = Column(Integer)
    shirts_uid = Column(Integer)
    shirts_num = Column(Integer)
    pants_uid = Column(Integer)
    pants_num = Column(Integer)
    sneakers_uid = Column(Integer)
    sneakers_num = Column(Integer)
    buy_sum = Column(Integer)


class Check(Base):
    __tablename__ = "Чек"
    uid = Column(Integer, autoincrement=True, primary_key=True, index=True)
    buyer_uid = Column(Integer)
    date = Column(DateTime, default=datetime.datetime.today())
    check_sum = Column(Integer)



class Buyer(Base):
    __tablename__ = "Покупатель"

    uid = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(Text)
    surname = Column(Text)
    discount = Column(Integer)
