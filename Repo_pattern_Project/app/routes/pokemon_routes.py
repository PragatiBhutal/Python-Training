from fastapi import APIRouter, Depends
from typing import Dict, List, Any
from app.Services.pokemon_service import PokemonService
from app.repository.pokemon_repository import pokemon_repository_instance
from app.schemas.pokemon_schema import PokemonUpdateInputOutput, PokemonGetPostInputOutput

router = APIRouter()


def get_pokemon_service() -> PokemonService:
    return PokemonService(pokemon_repository_instance)


@router.get("/pokemon", response_model=Dict[str, List[PokemonGetPostInputOutput]])
def get_all_pokemon(pokemon_service: PokemonService = Depends(get_pokemon_service)):
    return pokemon_service.get_all_pokemon()


@router.get("/pokemon/id/{pokemon_id}", response_model=PokemonGetPostInputOutput)
def get_pokemon_by_id(pokemon_id: int, pokemon_service: PokemonService = Depends(get_pokemon_service)):
    return pokemon_service.get_pokemon_by_id(pokemon_id)


@router.get("/pokemon/name/{pokemon_name}", response_model=PokemonGetPostInputOutput)
def get_pokemon_by_name(pokemon_name: str, pokemon_service: PokemonService = Depends(get_pokemon_service)):
    return pokemon_service.get_pokemon_by_name(pokemon_name)


@router.post("/pokemon", response_model=Dict[str, Any])
def create_pokemon(pokemon: PokemonGetPostInputOutput, pokemon_service: PokemonService = Depends(get_pokemon_service)):
    return pokemon_service.create_pokemon(pokemon.dict())


@router.put("/pokemon/{pokemon_id}", response_model=Dict[str, Any])
def update_pokemon(pokemon_id: int, updated_data: PokemonUpdateInputOutput,
                   pokemon_service: PokemonService = Depends(get_pokemon_service)):
    return pokemon_service.update_pokemon(pokemon_id, updated_data.dict(exclude_unset=True))


@router.delete("/pokemon/{pokemon_id}", response_model=Dict[str, Any])
def delete_pokemon(pokemon_id: int, pokemon_service: PokemonService = Depends(get_pokemon_service)):
    return pokemon_service.delete_pokemon(pokemon_id)
