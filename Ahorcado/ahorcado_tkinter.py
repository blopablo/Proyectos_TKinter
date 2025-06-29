# ------------- A H O R C A D O -------------------- #
# -------C o m p l e j o-----E n----T K I n t e r--- #

import tkinter as tk
from random import choice

class Ahorcado:
    def __init__(self):
        self.palabra = choice(["argentina", "bolivia", "brasil", "chile", "colombia", "ecuador", "paraguay", "peru", "uruguay", "venezuela"])
        self.adivinada = ["_"] * len(self.palabra)
        self.intentos = 6

        

        self.ventana = tk.Tk()
        self.ventana.title("Ahorcado")

        self.fondo = tk.PhotoImage(file="img\Ahorcado.png")  # Asegúrate que fondo.png esté en la misma carpeta
        self.canvas = tk.Canvas(self.ventana, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.fondo, anchor="nw")
        

        self.etiqueta_palabra = tk.Label(self.ventana, text=" ".join(self.adivinada), font=("Arial", 24))
        self.etiqueta_palabra.pack(pady=30)

        self.etiqueta_intentos = tk.Label(self.ventana, text=f"Intentos restantes: {self.intentos}", font=("Arial", 18))
        self.etiqueta_intentos.pack(pady=30)

        self.campo_letra = tk.Entry(self.ventana, font=("Arial", 18))
        self.campo_letra.pack(pady=30)

        self.boton_adivinar = tk.Button(self.ventana, text="adivinar", command=self.adivinar)
        self.boton_adivinar.pack(pady=30)

    def adivinar(self):
        letra = self.campo_letra.get()
        self.campo_letra.delete(0, tk.END)

        if len(letra) != 1:
            return
            
        if letra in self.palabra:
            for i, l in enumerate(self.palabra):
                if l == letra:
                    self.adivinada[i] = letra
        else:
            self.intentos -= 1

        self.etiqueta_palabra.config(text=" ".join(self.adivinada))
        self.etiqueta_intentos.config(text=f"Intentos restantes: {self.intentos}")

        if "_" not in self.adivinada:
            self.etiqueta_palabra.config(text="Adivinaste la palabra")
            self.etiqueta_intentos.config(state="disabled")
        elif self.intentos == 0:
            self.etiqueta_palabra.config(text=f"La palabra era: {self.palabra}. Juego terminado")
            self.boton_adivinar.config(state="disabled")

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    juego = Ahorcado()
    juego.run()