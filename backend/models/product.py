class Product:
    def __init__(self, nombre: str, imageProduct: str, isAvailable: bool, isFeaturedProduct: bool):

        self.nombre = nombre
        self.imageProduct = imageProduct
        self.isAvailable = isAvailable
        self.isFeaturedProduct = isFeaturedProduct

    #Getters    
        
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def imageProduct(self):
            return self._imageProduct
    
    @property
    def isAvailable(self):
            return self._isAvailable

    @property
    def isFeaturedProduct(self):
        return self._isFeaturedProduct
    
    #Setters

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @imageProduct.setter
    def imageProduct(self, nueva_imagen):
        self._imageProduct = nueva_imagen

    @isAvailable.setter
    def isAvailable(self, nuevo_estado):
        self._isAvailable = nuevo_estado

    @isFeaturedProduct.setter
    def isFeaturedProduct(self, nuevo_estado_destacado):
        self._isFeaturedProduct = nuevo_estado_destacado    
    
    #Print
    def __str__(self):
        return f'{self.nombre} {self.imageProduct} {self.isAvailable} {self.isFeaturedProduct}'