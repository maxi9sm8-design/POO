from vehiculo import Vehiculo

class Camioneta(Vehiculo):
    MODELOS = {
        "1": {
            "marca": "Ford",
            "modelo": "Raptor",
            "personas": 5,
            "traccion": "4x4 Terreno",
            "rendimiento": 9.2,
            "precio": 65000,
},
        "2": {
            "marca": "Toyota",
            "modelo": "Hilux",
            "personas": 5,
            "traccion": "AWD",
            "rendimiento": 11.5,
            "precio": 55000,
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
        seguro=12000,
):
        super().__init__(
            marca, modelo, precio, personas, traccion, rendimiento
)
        self.seguro = seguro

    def calcular_cotizacion(self, dias, pasajeros=0):
        print(f"incluye seguro 4x4 obligatorio: ${self.seguro:,.0f}/día")
        return (self.precio_diario + self.seguro) * dias