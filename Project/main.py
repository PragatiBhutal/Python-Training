from fastapi import FastAPI, HTTPException
from typing import Dict, Any, List
import requests

cache: Dict[str, Any] = {}
url = 'https://raw.githubusercontent.com/DetainedDeveloper/Pokedex/master/pokedex_raw/pokedex_raw_array.json'

response = requests.get(url)
if response.status_code == 200:
    cache["pokemon_data"] = response.json()
else:
    raise Exception("Failed to fetch Pokémon data")

app = FastAPI()

@app.get("/pokemon")
def get_all_pokemon():
    return {"pokemon_data": cache["pokemon_data"]}

@app.get("/pokemon/id/{pokemon_id}")
def get_pokemon_by_id(pokemon_id: int):
    for pokemon in cache["pokemon_data"]:
        if pokemon.get("id") == pokemon_id:
            return pokemon
    raise HTTPException(status_code=404, detail="Pokemon not found")

@app.get("/pokemon/name/{pokemon_name}")
def get_pokemon_by_name(pokemon_name: str):
    for pokemon in cache["pokemon_data"]:
        if pokemon.get("name", "").lower() == pokemon_name.lower():
            return pokemon
    raise HTTPException(status_code=404, detail="Pokemon not found")

@app.post("/pokemon")
def create_pokemon(pokemon: Dict[str, Any]):
    if not pokemon:
        raise HTTPException(status_code=400, detail="Pokemon data is empty")

    for existing_pokemon in cache["pokemon_data"]:
        if existing_pokemon.get("id") == pokemon.get("id"):
            raise HTTPException(status_code=400, detail="Pokemon with this ID already exists")

    cache["pokemon_data"].append(pokemon)

    return {"message": "Pokemon created successfully", "pokemon": pokemon}

@app.put("/pokemon/{pokemon_id}")
def update_pokemon(pokemon_id: int, updated_data: Dict[str, Any]):
    for pokemon in cache["pokemon_data"]:
        if pokemon.get("id") == pokemon_id:
            pokemon.update(updated_data)
            return {"message": "Pokemon updated successfully", "pokemon": pokemon}
    raise HTTPException(status_code=404, detail="Pokemon not found")

@app.delete("/pokemon/{pokemon_id}")
def delete_pokemon(pokemon_id: int):
    for index, pokemon in enumerate(cache["pokemon_data"]):
        if pokemon.get("id") == pokemon_id:
            deleted_pokemon = cache["pokemon_data"].pop(index)
            return {"message": "Pokemon deleted successfully", "pokemon": deleted_pokemon}
    raise HTTPException(status_code=404, detail="Pokemon not found")
