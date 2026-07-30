# 🚗 Sistema Inteligente de Alquiler y Cotización de Vehículos (POO en Python)

¡Bienvenido! Este proyecto es un sistema interactivo de consola en Python desarrollado para gestionar la recomendación y cotización automatizada de vehículos según las necesidades del cliente. 

El proyecto demuestra el uso práctico de los **4 pilares de la Programación Orientada a Objetos (POO)**.

---

## 🛠️ Pilares de POO Aplicados

1. **Abstracción**: Definición de la clase base abstracta `Vehiculo` (`ABC`) con atributos y métodos comunes para toda la flota.
2. **Encapsulamiento**: Protección de tarifas sensibles (`__precio_diario`) con modificadores y reglas de validación en los *setters* (no se permiten precios $\le 0$).
3. **Herencia**: Creación de las 4 categorías especializadas (`AutoSuv`, `Camioneta`, `Camion`, `Transporte`) que extienden de `Vehiculo`.
4. **Polimorfismo**: Implementación propia del método `calcular_cotizacion()` en cada categoría (aplicando descuentos por días, seguros 4x4, impuestos de carga o recargo por pasajeros).

