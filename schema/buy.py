from pydantic import BaseModel


class BuyBase(BaseModel):
    shirts_uid: int
    shirts_num: int
    pants_uid: int
    pants_num: int
    sneakers_uid: int
    sneakers_num: int
    buy_sum: int
    check_uid: int


class BuyCreate(BuyBase):
    pass


class BuyInDB(BuyBase):
    uid: int

    class Config:
        orm_mode = True


class Buy(BuyInDB):
    pass
