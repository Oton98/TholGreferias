class Producto:
    def __init__(self, id, nombre, tipo, codigo, descripcion, imagen, colores, manual, medidas, esta_disponible, es_destacado, coleccion_id):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.codigo = codigo
        self.descripcion = descripcion
        self.imagen = imagen
        self.colores = colores
        self.manual = manual
        self.medidas = medidas
        self.estaDisponible = esta_disponible
        self.esDestacado = es_destacado
        self.coleccion_id = coleccion_id