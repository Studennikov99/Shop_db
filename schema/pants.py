from pydantic import BaseModel


class PantsBase(BaseModel):
    pants_type: str
    pants_size: str
    pants_price: int
    pants_colour: str
    pants_in_stock: int
    pants_brand_name: str


class PantsCreate(PantsBase):
    pass


class PantsDelete(PantsBase):
    pass


class PantsInDB(PantsBase):
    uid: int

    class Config:
        orm_mode = True


class Pants(PantsInDB):
    pass
