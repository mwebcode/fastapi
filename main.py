import uvicorn
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float
  is_offer: Optional[bool] = None

@app.get('/')
def read_root():
  return {'Hello': 'World'}

@app.get('/hello/{name}')
def hello_name(name: str):
  return {'Hello': name}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
  return {'item_id': item_id, 'q': q}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
  return {'item_name': item.name, 'item_price': item.price, 'item_id': item_id}

uvicorn.run(app, host="0.0.0.0", port=8080)
