from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal, engine
from backend.models import Favorito, Base
from pydantic import BaseModel

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Permitir solicitudes desde el frontend (Live Server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O reemplazar con "http://127.0.0.1:5500" si querés restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Esquema de datos para POST
class FavoritoCreate(BaseModel):
    nombre: str
    comentario: str
    imagen_url: str

@app.post("/favoritos")
def crear_favorito(favorito: FavoritoCreate, db: Session = Depends(get_db)):
    nuevo = Favorito(**favorito.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@app.get("/favoritos")
def listar_favoritos(db: Session = Depends(get_db)):
    return db.query(Favorito).all()
