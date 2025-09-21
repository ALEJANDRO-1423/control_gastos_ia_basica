\# Conexión a MongoDB desde Python



\## Archivo: app/db.py



python

from pymongo import MongoClient



def get\_db():

&nbsp;   client = MongoClient("mongodb://localhost:27017/")

&nbsp;   db = client.control\_gastos

&nbsp;   return db





Uso:

python

Copiar código

from db import get\_db



db = get\_db()

print(db.list\_collection\_names())  # Muestra las colecciones existentes

