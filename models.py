import uuid
from typing import Optional
from pydantic import BaseModel, Field, validator
from typing import List
from bson.objectid import ObjectId as BsonObjectId

class PydanticObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls, v):
        if not isinstance(v, BsonObjectId):
            raise TypeError('ObjectId must be of bson ObjectId format')
        return str(v)

class Nonogram(BaseModel):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId(), alias="_id")
    values: List[List[bool]] = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": PydanticObjectId(),
                "values": [
                    [
                        True
                    ]
                ]
            }
        }

class NonogramUpdate(BaseModel):
    values: Optional[List[List[bool]]] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "values": [
                    [
                        True
                    ]
                ]
            }
        }