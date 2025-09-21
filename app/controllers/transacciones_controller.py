from app.db import get_db
from app.models.transaccion import Transaccion
from bson.objectid import ObjectId
from app.ia_categoria import predecir_categoria
from datetime import datetime

db = get_db()
transacciones_col = db.transacciones

# Crear transacción
def crear_transaccion(usuario_id, descripcion, monto, tipo="gasto", categoria=None):
    # Si es gasto y no se proporciona categoría, predecir con IA
    if tipo == "gasto" and not categoria:
        categoria = predecir_categoria(descripcion)
    
    transaccion = Transaccion(usuario_id, descripcion, monto, tipo)
    transaccion_dict = transaccion.to_dict()
    
    # Guardar categoría
    transaccion_dict["categoria"] = categoria
    # Guardar fecha actual UTC
    transaccion_dict["fecha"] = datetime.utcnow()
    
    result = transacciones_col.insert_one(transaccion_dict)
    return str(result.inserted_id)

# Obtener transacción por ID
def obtener_transaccion(transaccion_id):
    return transacciones_col.find_one({"_id": ObjectId(transaccion_id)})

# Actualizar transacción
def actualizar_transaccion(transaccion_id, descripcion=None, monto=None, tipo=None, categoria=None):
    update_data = {}
    if descripcion: update_data["descripcion"] = descripcion
    if monto: update_data["monto"] = monto
    if tipo: update_data["tipo"] = tipo
    if categoria: update_data["categoria"] = categoria
    if update_data:
        transacciones_col.update_one({"_id": ObjectId(transaccion_id)}, {"$set": update_data})

# Eliminar transacción
def eliminar_transaccion(transaccion_id):
    transacciones_col.delete_one({"_id": ObjectId(transaccion_id)})

# Listar todas las transacciones
def listar_transacciones():
    return list(transacciones_col.find())
