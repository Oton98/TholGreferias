from product import Producto

class Collection(Producto):

    def __init__(self, nombre: str, imageProduct: str, isAvailable: bool, isFeaturedProduct: bool, descriptionCollection1: str, descriptionCollection2: str, imgBanner: str, linkManualDetails: str, linkManualInstallation: str):
        super().__init__(nombre, imageProduct, isAvailable, isFeaturedProduct)

        self.descriptionCollection1 = descriptionCollection1
        self.descriptionCollection2 = descriptionCollection2
        self.imgBanner = imgBanner
        self.linkManualDetails = linkManualDetails
        self.linkManualInstallation = linkManualInstallation

    # Getters
    @property
    def descriptionCollection1(self):
        return self._descriptionCollection1

    @property
    def descriptionCollection2(self):
        return self._descriptionCollection2

    @property
    def imgBanner(self):
        return self._imgBanner

    @property
    def linkManualDetails(self):
        return self._linkManualDetails

    @property
    def linkManualInstallation(self):
        return self._linkManualInstallation

    # Setters
    @descriptionCollection1.setter
    def descriptionCollection1(self, nuevo_valor):
        self._descriptionCollection1 = nuevo_valor

    @descriptionCollection2.setter
    def descriptionCollection2(self, nuevo_valor):
        self._descriptionCollection2 = nuevo_valor

    @imgBanner.setter
    def imgBanner(self, nuevo_valor):
        self._imgBanner = nuevo_valor

    @linkManualDetails.setter
    def linkManualDetails(self, nuevo_valor):
        self._linkManualDetails = nuevo_valor

    @linkManualInstallation.setter
    def linkManualInstallation(self, nuevo_valor):
        self._linkManualInstallation = nuevo_valor

    #Printer
    def __str__(self):
        return f'{super().__str__()}, {self._descriptionCollection1}, {self._descriptionCollection2}, ' \
               f'{self._imgBanner}, {self._linkManualDetails}, {self._linkManualInstallation}'