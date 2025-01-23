from typing import Dict, Any, List

import requests


class PokemonRepository:
    def __init__(self):
        self.cache: Dict[str, Any] = {}
        self.url = 'https://raw.githubusercontent.com/DetainedDeveloper/Pokedex/master/pokedex_raw/pokedex_raw_array.json'

    def load_data(self):
        if "pokemon_data" not in self.cache:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.cache["pokemon_data"] = response.json()
            else:
                raise Exception("Failed to fetch Pokémon data")

    def get_all(self) -> List[Dict[str, Any]]:
        self.load_data()
        return self.cache["pokemon_data"]

    def get_by_id(self, pokemon_id: int) -> Dict[str, Any]:
        self.load_data()
        for pokemon in self.cache["pokemon_data"]:
            if pokemon.get("id") == pokemon_id:
                return pokemon
        return None

    def get_by_name(self, pokemon_name: str) -> Dict[str, Any]:
        self.load_data()
        for pokemon in self.cache["pokemon_data"]:
            if pokemon.get("name", "").lower() == pokemon_name.lower():
                return pokemon
        return None

    def create(self, pokemon: Dict[str, Any]):
        self.load_data()
        self.cache["pokemon_data"].append(pokemon)

    def update(self, pokemon_id: int, updated_data: Dict[str, Any]):
        self.load_data()
        for pokemon in self.cache["pokemon_data"]:
            if pokemon.get("id") == pokemon_id:
                pokemon.update(updated_data)
                return pokemon
        return None

    def delete(self, pokemon_id: int) -> Dict[str, Any]:
        self.load_data()
        for index, pokemon in enumerate(self.cache["pokemon_data"]):
            if pokemon.get("id") == pokemon_id:
                return self.cache["pokemon_data"].pop(index)
        return None


pokemon_repository_instance = PokemonRepository()
