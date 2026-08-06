# Sistema Cotizador de Alquiler de Vehiculos

Sistema interactivo desarrollado en Python para la gestion y cotizacion de alquileres de vehiculos segun la cantidad de pasajeros, dias de arrendamiento y tipo de terreno[cite: 1, 2]. Ofrece tanto una interfaz grafica moderna como un modo de consola interactivo[cite: 1, 2].

---

## Caracteristica Principal: Arquitectura POO

El proyecto aplica los pilares de la Programacion Orientada a Objetos (POO):

* Abstraccion: Definicion de la plantilla abstracta Vehiculo mediante el modulo abc[cite: 4].
* Encapsulamiento: Proteccion de la variable interna __precio_diario con validaciones en su @property y @setter para evitar tarifas invalidas[cite: 4].
* Herencia y Polimorfismo: Las clases hijas (AutoSuv, Camioneta, Camion, Transporte) heredan de Vehiculo y sobreescriben el metodo calcular_cotizacion agregando reglas de negocio especificas[cite: 3, 4, 5, 6, 7]:
  - AutoSuv: Descuento del 10% para estadias mayores a 7 dias[cite: 5].
  - Camioneta: Cargo diario por seguro obligatorio[cite: 7].
  - Camion: Impuesto unico adicional por carga pesada[cite: 6].
  - Transporte: Recargo dinamico por servicio a grupo segun la cantidad de pasajeros[cite: 3].

---

## Funcionalidades de la App

* Sugerencia Automatica de Capacidad: Si los pasajeros superan el limite del vehiculo elegido, el programa sugiere cambiar a la categoria de Transporte[cite: 1, 2].
* Limite Maximo: Restriccion estricta hasta un maximo de 28 pasajeros[cite: 2].
* Doble Interfaz:
  - GUI Moderna: Desarrollada con CustomTkinter y Tkinter[cite: 2].
  - Modo Consola: Menu por linea de comandos para ejecuciones rapidas[cite: 1].

---

## Estructura del Proyecto

* vehiculo: Clase base abstracta Vehiculo[cite: 4].
* auto_suv: Implementacion de autos urbanos/SUV[cite: 5].
* camioneta: Implementacion de vehiculos 4x4 / terreno[cite: 7].
* camion: Implementacion de transporte de carga[cite: 6].
* transporte: Implementacion de vans y buses de pasajeros[cite: 3].
* tk: Interfaz grafica con CustomTkinter[cite: 2].
* main: Flujo de consola interactivo[cite: 1].

---

## Requisitos e Instalacion

### Prerrequisitos
* Python 3.10 o superior.

### Instalacion
1. Clona el repositorio:
   git clone https://github.com/tu-usuario/cotizador-vehiculos.git
   cd cotizador-vehiculos

2. Instala la dependencia de CustomTkinter:
   pip install customtkinter

---

## Uso

### Ejecutar Interfaz Grafica (GUI)
python tk

### Ejecutar Version Consola
python main
