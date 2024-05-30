from functools import lru_cache
import time
from backend.models.collection import Coleccion
from backend.models.product import Producto

CACHE_EXPIRATION = 8 * 60 * 60
last_cache_update = 0

colecciones_cache = []
productos_cache = []

@lru_cache(maxsize=1)
def cargar_datos_en_cache():
    global last_cache_update
    global colecciones_cache
    global productos_cache
    
    current_time = time.time()

    # Verificar si el caché ha expirado
    if current_time - last_cache_update > CACHE_EXPIRATION:
        last_cache_update = current_time
        # Limpiar el caché actual
        cargar_datos_en_cache.cache_clear()
        # Obtener nuevos datos y guardar en el caché
        colecciones = Coleccion.query.filter(Coleccion.esta_eliminada == False).all()
        productos = Producto.query.filter(Producto.estaDisponible == True).all()
        colecciones_cache = colecciones
        productos_cache = productos
        return colecciones, productos
    else:
        return colecciones_cache, productos_cache

# Esto se ejecutará al cargar el módulo
colecciones_cache, productos_cache = cargar_datos_en_cache()