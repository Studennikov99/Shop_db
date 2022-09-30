from typing import TypeVar, Type

from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.main import Base

ModelType = TypeVar("ModelType", bound=Base)
SchemaType = TypeVar("SchemaType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
DeleteSchemaType = TypeVar("DeleteSchemaType", bound=BaseModel)


class CRUDBase:
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def delete(self, db: Session, filtered_field, value) -> SchemaType:
        db_obj = db.query(self.model).filter(getattr(self.model, filtered_field) == value).first()
        db.delete(db_obj)
        db.commit()
        return db_obj

    def check_five(self, db: Session, filtered_field_1, value_1,
                   filtered_field_2, value_2, filtered_field_3, value_3,
                   filtered_field_4, value_4, filtered_field_5, value_5):
        return db.query(self.model).filter((getattr(self.model, filtered_field_1) == value_1),
                                           (getattr(self.model, filtered_field_2) == value_2),
                                           (getattr(self.model, filtered_field_3) == value_3),
                                           (getattr(self.model, filtered_field_4) == value_4),
                                           (getattr(self.model, filtered_field_5) == value_5)).first()

    def check_two(self, db: Session, filtered_field_1, value_1,
                  filtered_field_2, value_2):
        return db.query(self.model).filter((getattr(self.model, filtered_field_1) == value_1),
                                           (getattr(self.model, filtered_field_2) == value_2)).first()

    def create(self, db: Session, obj_schema: CreateSchemaType) -> SchemaType:
        db_obj = self.model(**obj_schema.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, filtered_field, value):
        return db.query(self.model).filter(getattr(self.model, filtered_field) == value).first()

    def get_all(self, db: Session, filtered_field, value):
        return db.query(self.model).filter(getattr(self.model, filtered_field) == value).all()

    def get_all_field(self, db: Session, filtered_field):
        return db.query(self.model).order_by(filtered_field).all()

    def get_all_field_by_one(self, db: Session, filtered_field, value, order_field):
        return db.query(self.model).filter(getattr(self.model, filtered_field) == value).order_by(order_field).all()


    def update(self, db: Session, obj_schema: UpdateSchemaType) -> SchemaType:
        db_obj = self.model(**obj_schema.dict())
        db.commit()
        db.refresh(db_obj)
        return db_obj
