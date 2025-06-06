from pydantic import BaseModel

class ItemBase(BaseModel):
    nome: str
    descricao: str

class ItemCreate(ItemBase):
    pass

class ItemOut(ItemBase):
    id: int

    class Config:
        orm_mode = True
