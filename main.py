from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from config.db import session
from sqlalchemy import text
from models.clothe import Clothe


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,  
    allow_methods=["*"],  
    allow_headers=["*"],  
)


app.title = "lolas back_end"

@app.get("/check_connection")
def check_connection():
    with session:
        result = session.execute(text("SELECT 1")).scalar()
        return {"connection": "successful" if result == 1 else "failed"}


@app.get("/", tags=["home"])
def home():
    return "hola mundo"

# @app.get("/clothes", tags=["clothes"])
# def get_clothes():
#     db_clothes = session.query(Clothe).all()
#     return db_clothes


@app.get("/clothes", tags=["clothes"])
def get_clothes():
    db_clothes = session.query(Clothe).all()
    return db_clothes


@app.get("/clothes/{id}", tags=["clothes"])
def get_clothes_by_id(id: int):
    db_clothe = session.query(Clothe).filter(Clothe.id == id).first()
    print(db_clothe)
    return db_clothe


# en esta se hacen busquedas con qerys
@app.get("/clothes/", tags=["clothes"])
def get_clothes_by_brand(brand: str):
    db_clothes = session.query(Clothe).filter(Clothe.marca == brand).all()
    return db_clothes


@app.post("/clothes", tags=["clothes"])
def post_clothe(
    id: int = Body(),
    type: str = Body(),
    size: str = Body(),
    color: str = Body(),
    img_url: str = Body(),
    brand: str = Body(),
    condition: str = Body(),
    price: float = Body(),
    available: bool = Body(),
):
    db_clothe = Clothe(
        type=type,
        size=size,
        color=color,
        img_url=img_url,
        brand=brand,
        condition=condition,
        price=price,
        available=available,
    )
    session.add(db_clothe)
    session.commit()
    return {"Clothe added": db_clothe}

@app.put("/clothes/{id}", tags=["clothes"])
def put_clothe(
    id: int,
    type: str = Body(),
    size: str = Body(),
    color: str = Body(),
    img_url: str = Body(),
    brand: str = Body(),
    condition: str = Body(),
    price: float = Body(),
    available: bool = Body(),
):
    db_clothe = session.query(Clothe).filter(Clothe.id == id).first()

    if not db_clothe:
        return {"error": "Clothe not found"}

    if type != db_clothe.type:
        db_clothe.type = type
    if size != db_clothe.size:
        db_clothe.size = size
    if color != db_clothe.color:
        db_clothe.color = color
    if img_url != db_clothe.img_url:
        db_clothe.img_url = img_url
    if brand != db_clothe.brand:
        db_clothe.brand = brand
    if condition != db_clothe.condition:
        db_clothe.condition = condition
    if price != db_clothe.price:
        db_clothe.price = price
    if available is not None:
        db_clothe.available = available

    session.commit()
    session.refresh(db_clothe)
    return db_clothe


# @app.patch("/clothes/{id}", tags=["clothes"])
# def patch_clothe(
#     # None como valor por defecto, indicando que el campo es opcional
#     id: int,
#     type: str = Body(None),
#     size: str = Body(None),
#     color: str = Body(None),
#     img_url: str = Body(None),
#     brand: str = Body(None),
#     condition: str = Body(None),
#     price: float = Body(None),
#     available: bool = Body(None),
# ):
#     db_clothe = session.query(Clothe).filter(Clothe.id == id).first()

#     # Solo actualizamos los campos que fueron enviados
#     if type is not None:
#         db_clothe.type = type
#     if size is not None:
#         db_clothe.size = size
#     if color is not None:
#         db_clothe.color = color
#     if img_url is not None:
#         db_clothe.img_url = img_url
#     if brand is not None:
#         db_clothe.brand = brand
#     if condition is not None:
#         db_clothe.condition = condition
#     if price is not None:
#         db_clothe.price = price
#     if available is not None:
#         db_clothe.available = available

#     session.commit()
#     session.refresh(db_clothe)
#     return db_clothe


@app.patch("/clothes/{id}", tags=["clothes"])
def patch_clothe(
    id: int,
    type: str = (None),
    size: str = (None),
    color: str = (None),
    img_url: str = (None),
    brand: str = (None),
    condition: str = (None),
    price: float = (None),
    available: bool = (None),
):
    db_clothe = session.query(Clothe).filter(Clothe.id == id).first()
    
    print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    print(patch_clothe)
    print(db_clothe)

    # Only update fields with values in the request body
    if type:
        db_clothe.type = type
    if size:
        db_clothe.size = size
    if color:
        db_clothe.color = color
    if img_url:
        db_clothe.img_url = img_url
    if brand:
        db_clothe.brand = brand
    if condition:
        db_clothe.condition = condition
    if price:
        db_clothe.price = price
    if available:
        db_clothe.available = available
    
    session.commit()
    session.refresh(db_clothe)
    return db_clothe


@app.delete("/clothes/{id}", tags=["clothes"])
def delete_clothe(id: int):
    db_clothe = session.query(Clothe).filter(Clothe.id == id).first()
    session.delete(db_clothe)
    session.commit()
    return {"delete": "succesfuli"}