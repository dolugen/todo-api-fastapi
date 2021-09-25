from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db: list["TodoItem"] = {}


class TodoItem(BaseModel):
    id: int
    title: str


@app.get("/")
async def read_index():
    return list(db.values())


@app.get("/{item_id}")
async def read_one(item_id: int):
    return db[item_id]


@app.post("/")
async def create_new(item: TodoItem):
    db[item.id] = item
    return item
