from pydantic import BaseModel, Field
import pandera as pa
from pandera.engines.pandas_engine import PydanticModel


class Item(BaseModel):
    name: str
    price: int = Field(ge=1)


class ItemSchema(pa.SchemaModel):
    class Config:
        dtype = PydanticModel(Item)
        coerce = True
