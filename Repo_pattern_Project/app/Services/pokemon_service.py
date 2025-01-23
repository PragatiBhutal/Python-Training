from typing import Dict, Any
from fastapi import HTTPException
from app.repository.pokemon_repository import PokemonRepository


class PokemonService:
    def __init__(self, pokemon_repository: PokemonRepository):
        self.pokemon_repository = pokemon_repository

    def get_all_pokemon(self):
        return {"pokemon_data": self.pokemon_repository.get_all()}

    def get_pokemon_by_id(self, pokemon_id: int):
        pokemon = self.pokemon_repository.get_by_id(pokemon_id)
        if not pokemon:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        return pokemon

    def get_pokemon_by_name(self, pokemon_name: str):
        pokemon = self.pokemon_repository.get_by_name(pokemon_name)
        if not pokemon:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        return pokemon

    def create_pokemon(self, pokemon: Dict[str, Any]):
        if not pokemon:
            raise HTTPException(status_code=400, detail="Pokemon data is empty")
        if self.pokemon_repository.get_by_id(pokemon.get("id")):
            raise HTTPException(status_code=400, detail="Pokemon with this ID already exists")
        self.pokemon_repository.create(pokemon)
        return {"message": "Pokemon created successfully", "pokemon": pokemon}

    def update_pokemon(self, pokemon_id: int, updated_data: Dict[str, Any]):
        updated_pokemon = self.pokemon_repository.update(pokemon_id, updated_data)
        if not updated_pokemon:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        return {"message": "Pokemon updated successfully", "pokemon": updated_pokemon}

    def delete_pokemon(self, pokemon_id: int):
        deleted_pokemon = self.pokemon_repository.delete(pokemon_id)
        if not deleted_pokemon:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        return {"message": "Pokemon deleted successfully", "pokemon": deleted_pokemon}
