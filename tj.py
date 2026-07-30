from abc import ABC, abstractmethod

class Vehiculo(ABC):
    """Clase base de la cual heredan todos los vehículos."""
    
    def __init__(self, marca, modelo, precio, personas, traccion, rendimiento):
        self.marca = marca
        self.modelo = modelo
        self.personas = personas
        self.traccion = traccion
        self.rendimiento = rendimiento
        self.__precio_diario = 0.0
        self.precio_diario = precio  #llama al setter de abajo

    @property
    def precio_diario(self):
        return self.__precio_diario

    @precio_diario.setter
    def precio_diario(self, valor):
        # el valor solo puede ser mayor a 0
        if valor <= 0:
            print(f"el precio ${valor} no es valido, se le asigna tarifa base de $30.000")
            self.__precio_diario = 30000
        else:
            self.__precio_diario = valor
    @abstractmethod
    def calcular_cotizacion(self, dias, pasajeros=0):
        pass

    def mostrar_ficha(self):
        print("==================================================================")
        print(f"ficha tecnica {self.marca} {self.modelo}")
        print("=========================================================================")
        print(f" Capacidad   : {self.personas} personas")
        print(f" Tracción    : {self.traccion}")
        print(f" Rendimiento : {self.rendimiento} km/l")
        print(f" Precio/Día  : ${self.precio_diario:,.0f}")
        print("=========================================================================")
        
class AutoSuv(Vehiculo):
    MODELOS = {
        "1": {"marca": "Toyota", "modelo": "RAV4", "personas": 5, "traccion": "Urbana", "rendimiento": 14.5, "precio": 35000},
        "2": {"marca": "Hyundai", "modelo": "Tucson", "personas": 5, "traccion": "4x2", "rendimiento": 13.8, "precio": 32000}
    }

    def __init__(self, marca, modelo, precio, personas, traccion, rendimiento):
        super().__init__(marca, modelo, precio, personas, traccion, rendimiento)

    def calcular_cotizacion(self, dias, pasajeros=0):
        total = self.precio_diario * dias
        #descuento del 10% si usa por mas de 7 dias
        if dias > 7:
            desc = total * 0.10
            total = total - desc
            print(f"descuento del 10% aplicado: -${desc:,.0f}")
        return total


class Camioneta(Vehiculo):
    MODELOS = {
        "1": {"marca": "Ford", "modelo": "Raptor", "personas": 5, "traccion": "4x4 Terreno", "rendimiento": 9.2, "precio": 65000},
        "2": {"marca": "Toyota", "modelo": "Hilux", "personas": 5, "traccion": "AWD", "rendimiento": 11.5, "precio": 55000}
    }

    def __init__(self, marca, modelo, precio, personas, traccion, rendimiento, seguro=12000):
        super().__init__(marca, modelo, precio, personas, traccion, rendimiento)
        self.seguro = seguro

    def calcular_cotizacion(self, dias, pasajeros=0):
        print(f"incluye seguro 4x4: ${self.seguro:,.0f}/dia")
        return (self.precio_diario + self.seguro) * dias


class Camion(Vehiculo):
    MODELOS = {
        "1": {"marca": "Volvo", "modelo": "FH 16", "personas": 2, "traccion": "6x4", "rendimiento": 3.5, "precio": 120000},
        "2": {"marca": "Mercedes", "modelo": "Actros", "personas": 3, "traccion": "6x2", "rendimiento": 4.1, "precio": 100000}
    }

    def __init__(self, marca, modelo, precio, personas, traccion, rendimiento, impuesto=25000):
        super().__init__(marca, modelo, precio, personas, traccion, rendimiento)
        self.impuesto = impuesto

    def calcular_cotizacion(self, dias, pasajeros=0):
        print(f"Incluye impuesto de carga pesada: ${self.impuesto:,.0f}")
        return (self.precio_diario * dias) + self.impuesto

#definimos los autos con sus caracteristicas
class Transporte(Vehiculo):
    MODELOS = {
        "1": {"marca": "Mercedes", "modelo": "Sprinter Van", "personas": 15, "traccion": "Trasera", "rendimiento": 10.0, "precio": 80000},
        "2": {"marca": "Hyundai", "modelo": "County Bus", "personas": 28, "traccion": "4x2", "rendimiento": 7.5, "precio": 130000}
    }

    def __init__(self, marca, modelo, precio, personas, traccion, rendimiento):
        super().__init__(marca, modelo, precio, personas, traccion, rendimiento)

    def calcular_cotizacion(self, dias, pasajeros=0):
        if pasajeros == 0:
            pasajeros = self.personas
        recargo = 1500 * pasajeros
        print(f"recargo por {pasajeros} pasajeros: ${recargo:,.0f}")
        return (self.precio_diario * dias) + recargo


# sistema en si y cuestionario
class SistemaAlquiler:

    def crear_vehiculo(self, clase, datos):
        """Crea un objeto de la categoría recibida usando sus datos."""
        return clase(
            marca=datos["marca"],
            modelo=datos["modelo"],
            precio=datos["precio"],
            personas=datos["personas"],
            traccion=datos["traccion"],
            rendimiento=datos["rendimiento"]
        )

    def iniciar(self):
        print(" COTIZACION DE VEHICULOS")

        #preguntas
        try:
            pasajeros = int(input("¿Cuantas personas viajaran?: "))
            if pasajeros <= 0:
                print("ingrese un numero de personas valido")
                return

            print("\n2. ¿Qué terreno vas a recorrer?")
            print("   1 Ciudad")
            print("   2 Nieve / Playa / 4x4")
            print("   3 Trabajo Pesado / Carga")
            print("   4 Traslado de Grupo")
            opcion = input("   Seleccione una opción (1-4): ").strip()

            dias = int(input("¿cuantos dias durara el alquiler?: "))
            if dias <= 0:
                print("ingresar cantidad de dias")
                return

        except ValueError:
            print("ingresar numeros enteros")
            return

        # Elegir clase según opción
        if opcion == "1":
            clase_actual = AutoSuv
        elif opcion == "2":
            clase_actual = Camioneta
        elif opcion == "3":
            clase_actual = Camion
        elif opcion == "4":
            clase_actual = Transporte
        else:
            print("opcion no valida")
            return

        #sugerir la opcion por defecto
        datos_auto = clase_actual.MODELOS["1"]
        auto = self.crear_vehiculo(clase_actual, datos_auto)

        # verificar capacidad
        if pasajeros > auto.personas:
            print(f"el vehiculo seleccionado tiene capacidad para {auto.personas} personas")
            print("le sugerimos un vehiculo de la categoría Transporte mas grande")
            
            respuesta = input("¿Desea cotizar la opción más amplia? (Sí/No): ").strip().lower()

            if respuesta in ["si", "sí", "s"]:
                # se cambia el transporte dependiendo de las personas
                id_modelo = "2" if pasajeros > 15 else "1"
                datos_transporte = Transporte.MODELOS[id_modelo]
                auto = self.crear_vehiculo(Transporte, datos_transporte)
            else:
                print("cancelado por razones de seguridad")
                return

# la ficha y cotizacion
        auto.mostrar_ficha()
        total = auto.calcular_cotizacion(dias=dias, pasajeros=pasajeros)
        
        print(f"TOTAL A PAGAR: ${total:,.0f} CLP")

# ejecutar
if __name__ == "__main__":
    app = SistemaAlquiler()
    while True:
        app.iniciar()
        repetir = input("¿Desea hacer otra cotización? (Sí/No): ").strip().lower()
        if repetir not in ["si", "sí", "s"]:
            print("gracias por usar el sistema")
            break