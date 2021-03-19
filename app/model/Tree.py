from typing import Optional, List
from pydantic import BaseModel,Field


class createShoptreeModel(BaseModel):
    id: str = Field(min_length=3, max_length=3)
    name_tree:  str
    age_tree:   int
    catagroy:   str
    price:      str
    


class updateShoptreeModel(BaseModel):
    name_tree:Optional[str]  
    age_tree: Optional[int]
    catagroy: Optional[str]
    price:    Optional[int]


class createNameshoptreeModel(BaseModel):
    id: str = Field(min_length=3, max_length=3)
    name : str
    location : float


class updateNameshoptreeModel(BaseModel):
    name : Optional[str]
    location : Optional[float]
    
