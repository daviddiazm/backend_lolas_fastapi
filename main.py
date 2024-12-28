from fastapi import FastAPI, Body, Depends
from fastapi.middleware.cors import CORSMiddleware
# from config.db import session
from config.db import get_db
from sqlalchemy import text
from sqlalchemy.orm import Session
from models.clothe import Clothe


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,  
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# app.title = "lolas back_end"

@app.get("/check_connection")
def check_connection(db: Session = Depends(get_db)):
    with db:
        result = db.execute(text("SELECT 1")).scalar()
        return {"connection": "successful" if result == 1 else "failed"}


@app.get("/", tags=["home"])
def home():
    return "hola mundo"

# clothes

# obtiene todas las prendas
@app.get("/clothes", tags=["clothes"])
def get_clothes(db: Session = Depends(get_db)):
    db_clothes = db.query(Clothe).all()
    return db_clothes


# devulve los primeros 3
@app.get("/clothes_first_three", tags=["clothes"])
def get_clothes(db: Session = Depends(get_db)):
    db_clothes = db.query(Clothe).limit(3).all()
    return db_clothes


# se busca una prenda por el id
@app.get("/clothes/{id}", tags=["clothes"])
def get_clothes_by_id(id: int, db: Session = Depends(get_db)):
    db_clothe = db.query(Clothe).filter(Clothe.id == id).first()
    print(db_clothe)
    return db_clothe


# en esta se hacen busquedas con qerys
@app.get("/clothes/", tags=["clothes"])
def get_clothes_by_brand(brand: str, db: Session = Depends(get_db)):
    db_clothes = db.query(Clothe).filter(Clothe.marca == brand).all()
    return db_clothes


# sube una prenda
@app.post("/clothes", tags=["clothes"])
def post_clothe(
    db: Session = Depends(get_db),
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
    db.add(db_clothe)
    db.commit()
    return {"Clothe added": db_clothe}


# actualiza una prenda por id
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
    db: Session = Depends(get_db)
):
    db_clothe = db.query(Clothe).filter(Clothe.id == id).first()

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

    db.commit()
    db.refresh(db_clothe)
    return db_clothe


# actualiza la prenda por id con el patch
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
#     db: Session = Depends(get_db),
# ):
#     db_clothe = db.query(Clothe).filter(Clothe.id == id).first()
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

#     db.commit()
#     db.refresh(db_clothe)
#     return db_clothe


# actualiza la prenda por id con el patch
# @app.patch("/clothes/{id}", tags=["clothes"])
# def patch_clothe(
#     id: int,
#     type: str = (None),
#     size: str = (None),
#     color: str = (None),
#     img_url: str = (None),
#     brand: str = (None),
#     condition: str = (None),
#     price: float = (None),
#     available: bool = (None),
#     db: Session = Depends(get_db),
# ):
#     db_clothe = db.query(Clothe).filter(Clothe.id == id).first()
    
#     print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
#     print(patch_clothe)
#     print(db_clothe)

#     # Only update fields with values in the request body
#     if type:
#         db_clothe.type = type
#     if size:
#         db_clothe.size = size
#     if color:
#         db_clothe.color = color
#     if img_url:
#         db_clothe.img_url = img_url
#     if brand:
#         db_clothe.brand = brand
#     if condition:
#         db_clothe.condition = condition
#     if price:
#         db_clothe.price = price
#     if available:
#         db_clothe.available = available
    
#     db.commit()
#     db.refresh(db_clothe)
#     return db_clothe


# elimina una prenda por id
@app.delete("/clothes/{id}", tags=["clothes"])
def delete_clothe(id: int, db: Session = Depends(get_db)):
    db_clothe = db.query(Clothe).filter(Clothe.id == id).first()
    db.delete(db_clothe)
    db.commit()
    return {"delete": "succesfuli"}