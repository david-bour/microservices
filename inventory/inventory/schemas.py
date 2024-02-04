from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    name: str
    quantity: int = Field(default=0)

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    class Config:
        orm_mode = True