import customtkinter as ctk
from tkinter import messagebox
from auto_suv import AutoSuv
from camioneta import Camioneta
from camion import Camion
from transporte import Transporte

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class RentalAppGUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Cotizador de Alquiler")
        self.geometry("850x620")

        #diccionario vehiculos
        self.opciones = {
            "Auto ciudad": AutoSuv,
            "Camioneta": Camioneta,
            "Camion": Camion,
            "Transporte": Transporte,
        }

        #encabezado
        titulo = ctk.CTkLabel(
            self,
            text="Sistema Cotizador",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        titulo.pack(pady=10)

        #vista principal
        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, padx=15, pady=10)

        #preguntas 
        ctk.CTkLabel(frame, text="Pasajeros:").pack(anchor="w", padx=20)
        self.ent_pasajeros = ctk.CTkEntry(frame)
        self.ent_pasajeros.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(frame, text="Tipo de vehiculo:").pack(anchor="w", padx=20)
        self.cmb_tipo = ctk.CTkOptionMenu(
            frame, values=list(self.opciones.keys())
        )
        self.cmb_tipo.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(frame, text="Dias:").pack(anchor="w", padx=20)
        self.ent_dias = ctk.CTkEntry(frame)
        self.ent_dias.pack(fill="x", padx=20, pady=5)

        # boton
        btn = ctk.CTkButton(frame, text="Calcular", command=self.calcular)
        btn.pack(fill="x", padx=20, pady=15)

        # resultados
        self.txt = ctk.CTkTextbox(frame, height=180)
        self.txt.pack(fill="both", expand=True, padx=20, pady=10)

        self.lbl_total = ctk.CTkLabel(
            frame, text="Total: $0", font=ctk.CTkFont(size=16, weight="bold")
        )
        self.lbl_total.pack(pady=10)

    def calcular(self):
        # validaciones
        try:
            pasajeros = int(self.ent_pasajeros.get())
            dias = int(self.ent_dias.get())
        except:
            messagebox.showerror("datos invalidos")
            return

        if pasajeros <= 0 or dias <= 0:
            messagebox.showerror("deben ser numeros mayores a 0")
            return

        # maximo de 28
        if pasajeros > 28:
            messagebox.showwarning(
                "capacidad excedida", 
                "la capacidad maxima es de 28 personas"
            )
            return

        #la clase de vehiculo
        tipo = self.cmb_tipo.get()
        clase = self.opciones[tipo]

        # busca el carro recomendado por el n de ps
        dic_modelos = getattr(clase, "modelos", getattr(clase, "MODELOS", None))
        
        if not dic_modelos:
            messagebox.showerror(f"La clase {tipo} no tiene modelos definidos")
            return

        datos = dic_modelos["1"]

        #crear datos de carros
        auto = clase(
            datos["marca"],
            datos["modelo"],
            datos["precio"],
            datos["personas"],
            datos["traccion"],
            datos["rendimiento"],
        )

        #revisar capacidad del vehículo elegido
        if pasajeros > auto.personas:
            resp = messagebox.askyesno(
                "Aviso", "Supera capacidad, cambiar a transporte recomendado?"
            )
            if resp:
                dic_transporte = getattr(Transporte, "modelos", getattr(Transporte, "MODELOS", None))
                if pasajeros > 15:
                    datos = dic_transporte["2"]
                else:
                    datos = dic_transporte["1"]

                auto = Transporte(
                    datos["marca"],
                    datos["modelo"],
                    datos["precio"],
                    datos["personas"],
                    datos["traccion"],
                    datos["rendimiento"],
                )
            else:
                return

        #calculo de la cotizacion
        total = auto.calcular_cotizacion(dias, pasajeros)

        #formateo del texto 
        self.txt.delete("1.0", "end")

        texto = "RESUMEN\n"
        texto += f"Vehiculo: {auto.marca} {auto.modelo}\n"
        texto += f"Capacidad: {auto.personas}\n"
        texto += f"Dias: {dias}\n"
        texto += f"Pasajeros: {pasajeros}\n"

        self.txt.insert("1.0", texto)
        self.lbl_total.configure(text=f"Total: ${total} CLP")


if __name__ == "__main__":
    app = RentalAppGUI()
    app.mainloop()