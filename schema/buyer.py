from pydantic import BaseModel


class BuyerBase(BaseModel):
    name: str
    surname: str
    discount: int


class BuyerCreate(BuyerBase):
    pass


class BuyerInDB(BuyerBase):
    uid: int

    class Config:
        orm_mode = True


class Buyer(BuyerInDB):
    pass
