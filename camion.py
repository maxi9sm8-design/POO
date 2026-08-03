from vehiculo import Vehiculo

class Camion(Vehiculo):
    MODELOS = {
        "1": {
            "marca": "Volvo",
            "modelo": "FH 16",
            "personas": 2,
            "traccion": "6x4",
            "rendimiento": 3.5,
            "precio": 120000,
        },
        "2": {
            "marca": "Mercedes",
            "modelo": "Actros",
            "personas": 3,
            "traccion": "6x2",
            "rendimiento": 4.1,
            "precio": 100000,
            },
}

    def __init__(
        self,
        marca,
        modelo,
        precio,
        personas,
        traccion,
        rendimiento,
        impuesto=25000,
    ):
        super().__init__(
            marca, modelo, precio, personas, traccion, rendimiento
        )
        self.impuesto = impuesto

    def calcular_cotizacion(self, dias, pasajeros=0):
        print(f"incluye impuesto fijo por carga pesada: ${self.impuesto:,.0f} CLP")
        return (self.precio_diario * dias) + self.impuesto