from pydantic import BaseModel
from typing import List, Dict, Optional


class Ability(BaseModel):
    name: str
    is_hidden: bool


class Stat(BaseModel):
    name: str
    base_stat: int


class Type(BaseModel):
    name: str


class PokemonGetPostInputOutput(BaseModel):
    id: str
    name: str
    height: int
    weight: int
    xp: int
    image_url: str
    pokemon_url: str
    abilities: List[Ability]
    stats: List[Stat]
    types: List[Type]


class PokemonUpdateInputOutput(BaseModel):
    name: Optional[str] = None
    height: Optional[int] = None
    weight: Optional[int] = None
    xp: Optional[int] = None
    image_url: Optional[str] = None
    pokemon_url: Optional[str] = None
    abilities: Optional[List[Ability]] = None
    stats: Optional[List[Stat]] = None
    types: Optional[List[Type]] = None

