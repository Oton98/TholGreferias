class Coleccion:
    def __init__(self, id, nombre, img_monocomando, img_bimando, img_freestanding, img_accesorio, img_complemento, cantidad_productos=0, esta_eliminada=False): 
        self.id = id
        self.nombre = nombre
        self.img_monocomando = img_monocomando
        self.img_bimando =  img_bimando
        self.img_freestanding =  img_freestanding
        self.img_accesorio = img_accesorio
        self.img_complemento = img_complemento
        self.cantidad_productos = cantidad_productos
        self.esta_eliminada = esta_eliminada



