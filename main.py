from auto_suv import AutoSuv
from camion import Camion
from camioneta import Camioneta
from transporte import Transporte


class SistemaAlquiler:

    def crear_vehiculo(self, clase, datos):
        return clase(
            marca=datos["marca"],
            modelo=datos["modelo"],
            precio=datos["precio"],
            personas=datos["personas"],
            traccion=datos["traccion"],
            rendimiento=datos["rendimiento"],
        )

    def iniciar(self):
        print("COTIZACION DE VEHICULOS")

        try:
            pasajeros = int(input("Cuantas personas viajaran: "))
            if pasajeros <= 0:
                print("ingrese un numero valido de personas")
                return

            print("que terreno vas a recorrer?")
            print("1.Ciudad")
            print("2.Nieve / Playa / 4x4")
            print("3.Trabajo Pesado / Carga")
            print("4.Traslado de Grupo")
            opcion = input("seleccione una opcion (1 al 4): ").strip()

            dias = int(input("cuantos dias durara el alquiler?: "))
            if dias <= 0:
                print("ingrese una cantidad valida de dias")
                return

        except ValueError:
            print("entrada invalida")
            return

        if opcion == "1":
            clase_actual = AutoSuv
        elif opcion == "2":
            clase_actual = Camioneta
        elif opcion == "3":
            clase_actual = Camion
        elif opcion == "4":
            clase_actual = Transporte
        else:
            print(" Opción no válida.")
            return

        datos_auto = clase_actual.MODELOS["1"]
        auto = self.crear_vehiculo(clase_actual, datos_auto)

        if pasajeros > auto.personas:
            print(
                f"peligro: el vehículo seleccionado tiene capacidad maxima para {auto.personas} personas."
            )
            print(
                "Le sugerimos una alternativa de la categoria transporte con mayor capacidad."
            )
            respuesta = (
                input("desea cotizar la opcion mas amplia? (si/no): ")
                .strip()
                .lower()
            )

            if respuesta in ["si", "sí", "s"]:
                id_modelo = "2" if pasajeros > 15 else "1"
                datos_transporte = Transporte.MODELOS[id_modelo]
                auto = self.crear_vehiculo(Transporte, datos_transporte)
            else:
                print("Por razones de seguridad no podemos alquilar un vehículo sobrepoblado")
                return
        auto.mostrar_ficha()
        total = auto.calcular_cotizacion(dias=dias, pasajeros=pasajeros)
        print(f"el total a pagar es ${total:,.0f} CLP")


if __name__ == "__main__":
    app= SistemaAlquiler()
    while True:
        app.iniciar()
        repetir= (
            input("desea realizar otra cotizacion? (Si/No): ")
            .strip()
            .lower()
        )
        if repetir not in ["si", "sí", "s"]:
            print("gracias por usar nuestro sistema de alquiler")
            break