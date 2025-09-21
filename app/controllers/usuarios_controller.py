from app.db import get_db
from app.models.usuario import Usuario
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError
from datetime import datetime

db = get_db()
usuarios_col = db.usuarios

# Crear índice único en email
def asegurar_indice_email():
    usuarios_col.create_index("email", unique=True)

# Asegurar índice al importar el módulo
asegurar_indice_email()

def crear_usuario(nombre, email, password):
    # Comprobar si el email ya existe
    existente = usuarios_col.find_one({"email": email})
    if existente:
        return str(existente["_id"])  # Retornamos el ID existente

    # Crear usuario con password y fecha de creación
    usuario = Usuario(nombre, email, password)
    usuario_dict = usuario.to_dict()
    usuario_dict["fecha_creacion"] = datetime.utcnow()

    try:
        result = usuarios_col.insert_one(usuario_dict)
        return str(result.inserted_id)
    except DuplicateKeyError:
        # En caso raro de condición de carrera
        existente = usuarios_col.find_one({"email": email})
        return str(existente["_id"])

def obtener_usuario(usuario_id):
    return usuarios_col.find_one({"_id": ObjectId(usuario_id)})

def actualizar_usuario(usuario_id, nombre=None, email=None, password=None):
    update_data = {}
    if nombre:
        update_data["nombre"] = nombre
    if email:
        update_data["email"] = email
    if password:
        update_data["password"] = password
    if update_data:
        usuarios_col.update_one({"_id": ObjectId(usuario_id)}, {"$set": update_data})

def eliminar_usuario(usuario_id):
    usuarios_col.delete_one({"_id": ObjectId(usuario_id)})

def listar_usuarios():
    # Excluir el campo password al listar
    return list(usuarios_col.find({}, {"password": 0}))


