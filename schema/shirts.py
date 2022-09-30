from typing import Optional

from pydantic import BaseModel


class ShirtsBase(BaseModel):
    shirts_size: str
    shirts_type: str
    shirts_price: int
    shirts_colour: str
    shirts_in_stock: int
    shirts_brand_name: str


class ShirtsCreate(ShirtsBase):
    pass


class ShirtsInDB(ShirtsBase):
    uid: int

    class Config:
        orm_mode = True


class Shirts(ShirtsInDB):
    pass
