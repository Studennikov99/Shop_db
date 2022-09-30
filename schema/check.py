from pydantic import BaseModel
import datetime

class CheckBase(BaseModel):
    buyer_uid: int
    check_sum: int


class CheckCreate(CheckBase):
    pass


class CheckInDB(CheckBase):
    uid: int

    class Config:
        orm_mode = True


class Check(CheckInDB):
    pass
