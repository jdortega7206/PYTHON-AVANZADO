import tkinter as Ventana

class Formulario:
    def __init__(self):
        self.colorRojo = "red"
        self.colorAmarillo = "yellow"
        self.entries = {}
        self.datos_almacenados = []  # arreglo de almacenamiento
        self.formulario = None

    def iniciar_ventana(self):
        self.formulario = Ventana.Tk()
        self.formulario.title("Registro de Cliente.")
        self.formulario.geometry("700x550")
        self.formulario.resizable(False, False)
        self.formulario.configure(bg="red")
        self.formulario.configure(cursor="hand2")
        return self.formulario

    def iniciar_preguntas(self):
        campos = ["Nombre", "Apellido", "Email", "Teléfono", "Dirección"]
        y = 30
        for campo in campos:
            lbl = Ventana.Label(self.formulario, text=f"{campo}:", bg="yellow",
                                fg=self.colorRojo, font=("Arial", 14, "bold"))
            lbl.place(x=40, y=y)

            entry = Ventana.Entry(self.formulario, bg="yellow", fg="red",
                                  font=("Arial", 14), width=25)
            entry.place(x=180, y=y)
            self.entries[campo] = entry

            status = Ventana.Label(self.formulario, text="", bg="red",
                                   font=("Arial", 12), width=10)
            status.place(x=480, y=y)
            self.entries[campo + "_status"] = status
            y += 50

        Ventana.Button(self.formulario, text="Enviar", font=("Arial", 16, "bold"),
                       bg="blue", fg=self.colorAmarillo, width=15,
                       command=self.procesar_formulario).place(x=250, y=y + 10)

        self.lbl_resultado = Ventana.Label(self.formulario, text="", bg=self.colorAmarillo,
                                           font=("Arial", 12), justify="left", anchor="w")
        self.lbl_resultado.place(x=40, y=y + 70)

    def validar_campos(self):
        ok = True
        for campo in list(self.entries.keys()):
            if campo.endswith("_status"):
                continue
            valor = self.entries[campo].get().strip()
            status = self.entries[campo + "_status"]
            if valor == "":
                status.config(text="Vacío", fg="red")
                ok = False
            else:
                status.config(text="Válido", fg="green")
        return ok

    def capturar_datos(self):
        return [self.entries[c].get().strip() for c in self.entries if not c.endswith("_status")]

    def almacenar_datos(self, datos):
        self.datos_almacenados.append(datos)
        return self.datos_almacenados

    def imprimir_datos(self, datos):
        texto = "Datos registrados:\n" + "\n".join(f"{i+1}. {d}" for i, d in enumerate(datos))
        self.lbl_resultado.config(text=texto)

    def procesar_formulario(self):  # función general llamada por el botón
        if self.validar_campos():
            datos = self.capturar_datos()
            self.almacenar_datos(datos)
            self.imprimir_datos(datos)
        else:
            self.lbl_resultado.config(text="Complete todos los campos.")