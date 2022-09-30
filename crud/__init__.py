from crud.base import CRUDBase
from db.models import Shirts, Pants, Sneakers, Buy, Buyer, Check

shirts = CRUDBase(model=Shirts)
pants = CRUDBase(model=Pants)
sneakers = CRUDBase(model=Sneakers)
buy = CRUDBase(model=Buy)
buyer = CRUDBase(model=Buyer)
check = CRUDBase(model=Check)
