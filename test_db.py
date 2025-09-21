from app.db import get_db  # recuerda que db.py está dentro de app

db = get_db()
print(db.list_collection_names())
