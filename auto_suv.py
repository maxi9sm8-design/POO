from vehiculo import Vehiculo


class AutoSuv(Vehiculo):
    MODELOS = {
        "1": {
            "marca": "Toyota",
            "modelo": "RAV4",
            "personas": 5,
            "traccion": "Urbana",
            "rendimiento": 14.5,
            "precio": 35000,
        },
        "2": {
            "marca": "Hyundai",
            "modelo": "Tucson",
            "personas": 5,
            "traccion": "4x2",
            "rendimiento": 13.8,
            "precio": 32000,
        },
    }

    def __init__(self, marca, modelo, precio, personas, traccion, rendimiento):
        super().__init__(
            marca, modelo, precio, personas, traccion, rendimiento
        )

    def calcular_cotizacion(self, dias, pasajeros=0):
        total = self.precio_diario * dias
        if dias > 7:
            desc = total * 0.10
            total -= desc
            print(f" Descuento aplicado (10% por > 7 días): -${desc:,.0f} CLP")
        return total