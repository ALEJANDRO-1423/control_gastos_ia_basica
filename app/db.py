from pymongo import MongoClient

def get_db():
    """
    Función para conectar a la base de datos MongoDB.
    
    Retorna:
        db: objeto de la base de datos 'control_gastos'
    """
    client = MongoClient("mongodb://localhost:27017/")  # Cambia esta URL si usas MongoDB Atlas
    db = client.control_gastos
    return db
