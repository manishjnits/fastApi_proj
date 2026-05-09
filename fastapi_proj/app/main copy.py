# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Data model
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# In-memory "database"
items = []

# ✅ POST - Create item
@app.post("/items/")
def create_item(item: Item):
    # Check if item already exists
    for existing in items:
        if existing.id == item.id:
            raise HTTPException(status_code=400, detail="Item already exists")
    items.append(item)
    return {"message": "Item created successfully", "item": item}

# ✅ GET - Read all items
@app.get("/items/")
def get_items():
    return {"items": items}

# ✅ GET - Read single item
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Hi Manish Item not found in your local id")

# ✅ DELETE - Remove item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for item in items:
        if item.id == item_id:
            items.remove(item)
            return {"message": f"Item {item_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
