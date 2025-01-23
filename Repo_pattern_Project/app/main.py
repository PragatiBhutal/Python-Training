from fastapi import FastAPI
import uvicorn
from app.routes.pokemon_routes import router as pokemon_router

app = FastAPI()


app.include_router(pokemon_router)

if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=9000)
