from pydantic import BaseModel


class SneakersBase(BaseModel):
    sneakers_type: str
    sneakers_size: str
    sneakers_price: int
    sneakers_colour: str
    sneakers_in_stock: int
    sneakers_brand_name: str


class SneakersCreate(SneakersBase):
    pass


class SneakersUpdate(SneakersBase):
    pass


class SneakersInDB(SneakersBase):
    uid: int

    class Config:
        orm_mode = True


class Sneakers(SneakersInDB):
    pass
