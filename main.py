from fastapi import FastAPI, Body
from config.db import session
from sqlalchemy import text
from models.clothe import Clothe


app = FastAPI()

app.title = "lolas back_end"

# clothes = [
#     {
#         "id": 1,
#         "tipo": "Camiseta",
#         "talla": "M",
#         "color": "Blanco",
#         "material": "Algodón",
#         "marca": "H&M",
#         "condicion": "Buena",
#         "precio": 5.00,
#         "disponible": True,
#     },
#     {
#         "id": 2,
#         "tipo": "Jeans",
#         "talla": "32",
#         "color": "Azul",
#         "material": "Denim",
#         "marca": "Levi's",
#         "condicion": "Excelente",
#         "precio": 15.00,
#         "disponible": True,
#     },
#     {
#         "id": 3,
#         "tipo": "Chaqueta",
#         "talla": "L",
#         "color": "Negro",
#         "material": "Cuero sintético",
#         "marca": "Zara",
#         "condicion": "Buena",
#         "precio": 20.00,
#         "disponible": False,
#     },
#     {
#         "id": 4,
#         "tipo": "Vestido",
#         "talla": "S",
#         "color": "Rojo",
#         "material": "Poliéster",
#         "marca": "Forever 21",
#         "condicion": "Aceptable",
#         "precio": 12.00,
#         "disponible": True,
#     },
#     {
#         "id": 5,
#         "tipo": "Sudadera",
#         "talla": "XL",
#         "color": "Gris",
#         "material": "Algodón",
#         "marca": "Nike",
#         "condicion": "Buena",
#         "precio": 10.00,
#         "disponible": True,
#     },
#     {
#         "id": 6,
#         "tipo": "Falda",
#         "talla": "M",
#         "color": "Negro",
#         "material": "Lana",
#         "marca": "Uniqlo",
#         "condicion": "Excelente",
#         "precio": 8.00,
#         "disponible": True,
#     },
#     {
#         "id": 7,
#         "tipo": "Camisa",
#         "talla": "L",
#         "color": "Azul claro",
#         "material": "Algodón",
#         "marca": "Tommy Hilfiger",
#         "condicion": "Buena",
#         "precio": 14.00,
#         "disponible": False,
#     },
#     {
#         "id": 8,
#         "tipo": "chaqueta",
#         "talla": "L",
#         "color": "Azul claro",
#         "material": "Algodón",
#         "marca": "Tommy Hilfiger",
#         "condicion": "Buena",
#         "precio": 14.00,
#         "disponible": False,
#     },
# ]


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
#     return clothes

# @app.get("/clothes/{id}", tags=["clothes"])
# def get_clothes_by_id(id: int):
#     for clothe in clothes:
#         if clothe["id"] == id:
#             return clothe
#     return "no se encontro id"


# # en esta se hacen busquedas con qerys
# @app.get("/clothes/", tags=["clothes"])
# def get_clothes_by_brand(brand: str):
#     for clothe in clothes:
#         if clothe["marca"] == brand:
#             return clothe
#     return "no se encontro prendas de esa marca"


# @app.post("/clothes", tags=["clothes"])
# def post_clothe(
#     id: int = Body(),
#     tipo: str = Body(),
#     talla: str = Body(),
#     color: str = Body(),
#     material: str = Body(),
#     marca: str = Body(),
#     codicion: str = Body(),
#     precio: float = Body(),
#     disponible: bool = Body(),
# ):
#     clothes.append(
#         {
#             "id": id,
#             "tipo": tipo,
#             "talla": talla,
#             "color": color,
#             "material": material,
#             "marca": marca,
#             "condicion": codicion,
#             "precio": precio,
#             "disponible": disponible,
#         }
#     )
#     return clothes


# @app.put("/clothes/{id}", tags=["clothes"])
# def put_clothe(
#     id: int,
#     tipo: str = Body(),
#     talla: str = Body(),
#     color: str = Body(),
#     material: str = Body(),
#     marca: str = Body(),
#     codicion: str = Body(),
#     precio: float = Body(),
#     disponible: bool = Body(),
# ):
#     for clothe in clothes:
#         if id == clothe["id"]:
#             clothe["tipo"] = tipo
#             clothe["talla"] = talla
#             clothe["color"] = color
#             clothe["material"] = material
#             clothe["marca"] = marca
#             clothe["condicion"] = codicion
#             clothe["precio"] = precio
#             clothe["disponible"] = disponible
#     return clothes


# @app.delete("/clothes/{id}", tags=["clothes"])
# def delete_clothe(id: int):
#     for clothe in clothes:
#         if id == clothe["id"]:
#             clothes.remove(clothe)
#     return clothes


# con la base de datos

@app.get("/clothes", tags=["clothes"])
def get_clothes():
    db_clothes = session.query(Clothe).all()
    return db_clothes


@app.get("/clothes/{id}", tags=["clothes"])
def get_clothes_by_id(id: int):
    db_clothe = session.query(Clothe).filter(Clothe.id == id).first()
    return db_clothe


# en esta se hacen busquedas con qerys
@app.get("/clothes/", tags=["clothes"])
def get_clothes_by_brand(brand: str):
    db_clothes = session.query(Clothe).filter(Clothe.marca == brand).all()
    return db_clothes


@app.post("/clothes", tags=["clothes"])
def post_clothe(
    id: int = Body(),
    tipo: str = Body(),
    talla: str = Body(),
    color: str = Body(),
    material: str = Body(),
    marca: str = Body(),
    condicion: str = Body(),
    precio: float = Body(),
    disponible: bool = Body(),
):
    db_clothe = Clothe(
        tipo=tipo,
        talla=talla,
        color=color,
        material=material,
        marca=marca,
        condicion=condicion,
        precio=precio,
        disponible=disponible,
    )
    session.add(db_clothe)
    session.commit()
    return {"Clothe added": db_clothe}


# @app.put("/clothes/{id}", tags=["clothes"])
# def update_clothe(
#     id: int,
#     tipo: str = Body(),
#     talla: str = Body(),
#     color: str = Body(),
#     material: str = Body(),
#     marca: str = Body(),
#     condicion: str = Body(),
#     precio: float = Body(),
#     disponible: bool = Body()
# ):
#     db_Clothe = session.query(Clothe).filter(Clothe.id == id).first()
#     session.refresh(db_Clothe)
#     session.commit()
#     return {"Clothe added": db_Clothe}

@app.put("/clothes/{id}", tags=["clothes"])
def put_clothe(
    id: int,
    tipo: str = Body(),
    talla: str = Body(),
    color: str = Body(),
    material: str = Body(),
    marca: str = Body(),
    condicion: str = Body(),
    precio: float = Body(),
    disponible: bool = Body(),
):
    db_clothe = session.query(Clothe).filter(Clothe.id == id).first()

    if not db_clothe:
        return {"error": "Clothe not found"}

    if tipo != db_clothe.tipo:
        db_clothe.tipo = tipo
    if talla != db_clothe.talla:
        db_clothe.talla = talla
    if color != db_clothe.color:
        db_clothe.color = color
    if material != db_clothe.material:
        db_clothe.material = material
    if marca != db_clothe.marca:
        db_clothe.marca = marca
    if condicion != db_clothe.condicion:
        db_clothe.condicion = condicion
    if precio != db_clothe.precio:
        db_clothe.precio = precio
    if disponible is not None:
        db_clothe.disponible = disponible

    session.commit()
    session.refresh(db_clothe)
    return db_clothe


@app.patch("/clothes/{id}", tags=["clothes"])
def patch_clothe(
    id: int,
    tipo: str = Body(None),  # None como valor por defecto, indicando que el campo es opcional
    talla: str = Body(None),
    color: str = Body(None),
    material: str = Body(None),
    marca: str = Body(None),
    condicion: str = Body(None),
    precio: float = Body(None),
    disponible: bool = Body(None),
):
    # Obtener la prenda existente de la base de datos
    db_clothe = session.query(Clothe).filter(Clothe.id == id).first()

    # Solo actualizamos los campos que fueron enviados
    if tipo is not None:
        db_clothe.tipo = tipo
    if talla is not None:
        db_clothe.talla = talla
    if color is not None:
        db_clothe.color = color
    if material is not None:
        db_clothe.material = material
    if marca is not None:
        db_clothe.marca = marca
    if condicion is not None:
        db_clothe.condicion = condicion
    if precio is not None:
        db_clothe.precio = precio
    if disponible is not None:
        db_clothe.disponible = disponible

    session.commit()
    session.refresh(db_clothe)
    return db_clothe