from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self, marca, modelo, precio, personas, traccion, rendimiento):
        self.marca = marca
        self.modelo = modelo
        self.personas = personas
        self.traccion = traccion
        self.rendimiento = rendimiento
        self.__precio_diario = 0.0
        self.precio_diario = precio

    @property
    def precio_diario(self):
        return self.__precio_diario

    @precio_diario.setter
    def precio_diario(self, valor):
        if valor <= 0:
            print(f"[ALERTA] el precio ${valor} no es valido, dando tarifa base de $30.000")
            self.__precio_diario = 30000.0
        else:
            self.__precio_diario = float(valor)

    @abstractmethod
    def calcular_cotizacion(self, dias, pasajeros=0):
        pass

    def mostrar_ficha(self):
        print("============================================================")
        print(f" FICHA TÉCNICA: {self.marca} {self.modelo}")
        print("=" * 50)
        print(f" Capacidad   : {self.personas} personas")
        print(f" Tracción    : {self.traccion}")
        print(f" Rendimiento : {self.rendimiento} km/l")
        print(f" Precio/Día  : ${self.precio_diario:,.0f} CLP")
        print("========================================================")