from vehiculo import Vehiculo

class Transporte(Vehiculo):
    modelos= {
        "1": {
            "marca": "Mercedes",
            "modelo": "Sprinter Van",
            "personas": 15,
            "traccion": "Trasera",
            "rendimiento": 10.0,
            "precio": 80000,
        },
        "2": {
            "marca": "Hyundai",
            "modelo": "County Bus",
            "personas": 28,
            "traccion": "4x2",
            "rendimiento": 7.5,
            "precio": 130000,
        },
    }
    def __init__(self, marca, modelo, precio, personas, traccion, rendimiento):
        super().__init__(
            marca, modelo, precio, personas, traccion, rendimiento
        )
    def calcular_cotizacion(self, dias, pasajeros=0):
        if pasajeros <= 0:
            pasajeros = self.personas
        recargo = 1500 * pasajeros
        print(f" Recargo por servicio a grupo ({pasajeros} pasajeros): ${recargo:,.0f} CLP")
        return (self.precio_diario * dias) + recargo