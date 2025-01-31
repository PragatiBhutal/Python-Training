from fastapi import FastAPI
import uvicorn


from v1.database.todo_db import Base, engine
from v1.routes.todo_routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

# if __name__ == "__main__":
#     uvicorn.run(app="main:app", host="127.0.0.1", port=9000)
