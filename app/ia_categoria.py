# Definición de categorías y palabras clave asociadas
CATEGORIAS = {
    "comida": ["restaurante", "café", "almuerzo", "desayuno", "cena"],
    "transporte": ["taxi", "bus", "metro", "gasolina", "uber"],
    "entretenimiento": ["cine", "película", "teatro", "concierto", "videojuego"],
    "hogar": ["supermercado", "agua", "luz", "internet", "renta"],
    "salud": ["farmacia", "medicina", "doctor", "hospital"]
}

# Función para predecir categoría a partir de la descripción
def predecir_categoria(descripcion):
    descripcion = descripcion.lower()
    for categoria, palabras in CATEGORIAS.items():
        for palabra in palabras:
            if palabra in descripcion:
                return categoria
    return "otros"
