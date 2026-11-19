from fastapi import FastAPI, HTTPException, Header, Depends, Query
from pydantic import BaseModel, Field

app = FastAPI(title="ShopEasy API", version="1.0")

class ProductIn(BaseModel):
    name: str = Field(min_length=2, max_length=60)
    price: float = Field(gt=0, description="Price in rupees")
    in_stock: bool = True

class Product(ProductIn):
    id: int

DB: dict[int, Product] = {
    1: Product(id=1, name="Steel Bottle", price=499),
    2: Product(id=2, name="Yoga Mat", price=1299),
    3: Product(id=3, name="Desk Lamp", price=899, in_stock=False),
}

def require_key(x_api_key: str = Header(default="")):
    if x_api_key != "demo-key":
        raise HTTPException(status_code=401, detail="Send header X-API-Key: demo-key")

@app.get("/products", response_model=list[Product])
def list_products(max_price: float | None = Query(default=None, gt=0), in_stock: bool | None = None):
    items = DB.values()
    if max_price is not None:
        items = [p for p in items if p.price <= max_price]
    if in_stock is not None:
        items = [p for p in items if p.in_stock == in_stock]
    return list(items)

@app.get("/products/{pid}", response_model=Product)
def get_product(pid: int):
    if pid not in DB:
        raise HTTPException(status_code=404, detail="Product not found")
    return DB[pid]

@app.post("/products", response_model=Product, status_code=201, dependencies=[Depends(require_key)])
def create_product(item: ProductIn):
    new = Product(id=max(DB) + 1, **item.model_dump())
    DB[new.id] = new
    return new