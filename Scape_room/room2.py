import tkinter as tk
from tkinter import messagebox
import os
import pygame

class Room:
    def __init__(self):

        pygame.mixer.init()
        pygame.mixer.music.load("sound/fondo.mp3")
        pygame.mixer.music.get_volume()
        pygame.mixer.music.play(-1)

        self.sonido_click = pygame.mixer.Sound("sound/susurro.mp3",)
        self.sonido_click1 = pygame.mixer.Sound("sound/calle.mp3",)
        self.sonido_click2 = pygame.mixer.Sound("sound/suelo1.mp3")
        self.sonido_click3 = pygame.mixer.Sound("sound/tv.mp3")
        self.sonido_click4 = pygame.mixer.Sound("sound/abrir_cajon.mp3")
        self.sonido_click5 = pygame.mixer.Sound("sound/mueble.mp3")
        self.sonido_click6 = pygame.mixer.Sound("sound/door.mp3")

        self.ventana = tk.Tk()
        self.ventana.title("Madness")
        self.ventana.geometry("800x800")
        self.ventana.resizable(False, False)

        # Fondo
        fondo_path = os.path.join("img", "room.png")
        try:
            self.fondo_img = tk.PhotoImage(file=fondo_path)
            self.fondo_label = tk.Label(self.ventana, image=self.fondo_img)
            self.fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
        except tk.TclError:
            messagebox.showerror("Error", f"No se pudo cargar la imagen de fondo: {fondo_path}")
            

        # Cargar imágenes para botones
        self.imgs = []  # Lista para mantener las referencias
        img_files = [
            "1.png", "2.png", "3.png",
            "4.png", "5.png", "5.png"
        ]

        for img_file in img_files:
            img_path = os.path.join("img", img_file)
            try:
                img = tk.PhotoImage(file=img_path)
                self.imgs.append(img)
            except tk.TclError:
                messagebox.showerror("Error", f"No se pudo cargar la imagen: {img_path}")
                self.imgs.append(None)

        # Crear botones con imágenes
        self.boton1 = tk.Button(self.ventana, image=self.imgs[5], compound="top", # - - - , text="enigma 1"
                                font=("Arial", 12), bg="white", fg="black", width=10, height=10, command=self.abrir_emergente)
        self.boton1.place(x=400, y=50)

        self.boton2 = tk.Button(self.ventana, image=self.imgs[5], compound="top", # - - - , text="enigma 1"
                                font=("Arial", 12), bg="white", fg="black", width=10, height=10, command=self.abrir_emergente1)
        self.boton2.place(x=425, y=550)

        self.boton3 = tk.Button(self.ventana, image=self.imgs[5], compound="top", # - - - , text="enigma 2"
                                font=("Arial", 12), bg="white", fg="black", width=10, height=10, command=self.abrir_emergente2)
        self.boton3.place(x=150, y=200)

        self.boton4 = tk.Button(self.ventana, image=self.imgs[5], compound="top", # - - - , text="enigma 3"
                                font=("Arial", 12), bg="white", fg="black", width=10, height=10, command=self.tv)
        self.boton4.place(x=600, y=270)

        self.boton5 = tk.Button(self.ventana, image=self.imgs[5], compound="top", # - - - , text="enigma 4"
                                font=("Arial", 12), bg="white", fg="black", width=10, height=10, command=self.mueble)
        self.boton5.place(x=10, y=500)

        self.boton6 = tk.Button(self.ventana, image=self.imgs[5], compound="top", # - - - , text="enigma 5"
                                font=("Arial", 12), bg="white", fg="black", width=10, height=10, command=self.puerta)
        self.boton6.place(x=350, y=270)

# - - - - T E C H O - - - - #

    def abrir_emergente(self):
        # Crear ventana emergente
        self.sonido_click.play()
        emergente = tk.Toplevel(self.ventana)
        emergente.title("Alguien escribio en el techo . . . ")
        emergente.geometry("600x600")
        emergente.resizable(False, False)

        # Ruta de la imagen de fondo
        fondo_emergente_path = os.path.join("img", "1.png")
        try:
            fondo_emergente_img = tk.PhotoImage(file="img/1.png") # - - - estaba usando \ y python lo reconoce como otra funcion (carácter de escape)
            fondo_emergente_label = tk.Label(emergente, image=fondo_emergente_img, width=800, height=800)
            fondo_emergente_label.image = fondo_emergente_img  # Para evitar que la imagen se elimine por el recolector de basura
            fondo_emergente_label.place(x=0, y=0, relwidth=1, relheight=1)
        except tk.TclError:
            messagebox.showerror("Error", f"No se pudo cargar la imagen emergente: {fondo_emergente_path}")

# - - - - P I S O - - - - #

    def abrir_emergente1(self):
        self.sonido_click2.play()
        emergente1 = tk.Toplevel(self.ventana)
        emergente1.title("Puedo ver algo escrito en el suelo. . . ")
        emergente1.geometry("600x600")
        emergente1.resizable(False, False)

        # Ruta de la imagen de fondo
        fondo_emergente1_path = os.path.join("img", "2.png")
        try:
            fondo_emergente1_img = tk.PhotoImage(file="img/2.png") # - - - estaba usando \ y python lo reconoce como otra funcion (carácter de escape)
            fondo_emergente1_label = tk.Label(emergente1, image=fondo_emergente1_img, width=500, height=500)
            fondo_emergente1_label.image = fondo_emergente1_img  # Para evitar que la imagen se elimine por el recolector de basura
            fondo_emergente1_label.place(x=0, y=0, relwidth=1, relheight=1)
        except tk.TclError:
            messagebox.showerror("Error", f"No se pudo cargar la imagen emergente: {fondo_emergente1_path}")

# - - - - V E N T A N A - - - - #

    def abrir_emergente2(self):
        self.sonido_click.play()
        # Crear ventana emergente
        emergente2 = tk.Toplevel(self.ventana)
        emergente2.title("Aparentemente aquí hay que colocar alguna especie de codigo")
        emergente2.geometry("800x800")
        emergente2.resizable(False, False)

        # Ruta de la imagen de fondo
        fondo_emergente2_path = os.path.join("img", "3.png")
        try:
            fondo_emergente2_img = tk.PhotoImage(file="img/3.png") # - - - estaba usando \ y python lo reconoce como otra funcion (carácter de escape)
            fondo_emergente2_label = tk.Label(emergente2, image=fondo_emergente2_img, width=500, height=500)
            fondo_emergente2_label.image = fondo_emergente2_img  # Para evitar que la imagen se elimine por el recolector de basura
            fondo_emergente2_label.place(x=0, y=0, relwidth=1, relheight=1)
        except tk.TclError:
            messagebox.showerror("Error", f"No se pudo cargar la imagen emergente: {fondo_emergente2_path}")

        # Campo de usuario
        # - - - tk.Label(emergente2, text="Punta", bg="darkslategray", font=("Arial", 14)).place(x=370, y=50)
        entry_usuario = tk.Entry(emergente2, font=("Arial", 14), text="Punta", width=5, bg="darkslategray", fg="red")
        entry_usuario.place(x=370, y=310)

    # Campo de contraseña
        # - - - tk.Label(emergente2, text="Space", bg="darkslategray", font=("Arial", 14)).place(x=150, y=400)
        entry_contraseña = tk.Entry(emergente2, font=("Arial", 14), width=5, bg="darkslategray", fg="red")
        entry_contraseña.place(x=370, y=400)

    # Función para validar
        def validar_credenciales():
            usuario = entry_usuario.get()
            contraseña = entry_contraseña.get()
            if usuario == "07103" and contraseña == "18410":
                messagebox.showinfo("Abrir la persiana, aunque la ventana permanece cerrada...", "Se logra ver algo escrito en la pared de enfrente...")
                self.ventana_secreta()
                emergente2.destroy()
            else:
                messagebox.showerror("No se mueve...", "Se ve que algo estoy haciendo mal...")

    # Botón de acceso
        boton_login = tk.Button(emergente2, text="Acc£Ðer", bg="darkslategray", font=("Arial", 14), command=validar_credenciales)
        boton_login.place(x=350, y=600)



# - - - - C A L L E - - - - #

    def ventana_secreta(self):
        self.sonido_click1.play()
        secreta = tk.Toplevel(self.ventana)
        secreta.title("No recuerdo conocer este lugar...")
        secreta.geometry("800x800")
        secreta.resizable(False, False)

        # Ruta de la imagen de fondo
        secreta_path = os.path.join("img", "ah.png")
        try:
            fondo_secreta_img = tk.PhotoImage(file="img/ah.png") # - - - estaba usando \ y python lo reconoce como otra funcion (carácter de escape)
            fondo_secreta_label = tk.Label(secreta, image=fondo_secreta_img, width=800, height=800)
            fondo_secreta_label.image = fondo_secreta_img  # Para evitar que la imagen se elimine por el recolector de basura
            fondo_secreta_label.place(x=0, y=0, relwidth=1, relheight=1)
        except tk.TclError:
            messagebox.showerror("Error", f"No se pudo cargar la imagen emergente: {fondo_emergente_path}")

# - - - - T V - - - - #

    def tv(self):
        self.sonido_click3.play(1)
        emergente3 = tk.Toplevel(self.ventana)
        emergente3.title("La tv funciona, pero no se logra ver nada")
        emergente3.geometry("800x800")
        emergente3.resizable(False, False)

        # Ruta de la imagen de fondo
        fondo_emergente3_path = os.path.join("img", "tv.png")
        try:
            fondo_emergente3_img = tk.PhotoImage(file="img/tv.png") # - - - estaba usando \ y python lo reconoce como otra funcion (carácter de escape)
            fondo_emergente3_label = tk.Label(emergente3, image=fondo_emergente3_img, width=500, height=500)
            fondo_emergente3_label.image = fondo_emergente3_img  # Para evitar que la imagen se elimine por el recolector de basura
            fondo_emergente3_label.place(x=0, y=0, relwidth=1, relheight=1)
        except tk.TclError:
            messagebox.showerror("Error", f"No se pudo cargar la imagen emergente: {fondo_emergente3_path}")

        entry_contraseña = tk.Entry(emergente3, font=("Arial", 20), width=7, bg="black", fg="red")
        entry_contraseña.place(x=100, y=545)

    # Función para validar
        def validar_credenciales1():
            contraseña = entry_contraseña.get()
            if contraseña == "ch33":
                messagebox.showinfo("Cambio la señal de la TV, pero sigue igual...", "Espéara, noto que cambio algo en el color...")
                self.tv1()
                emergente3.destroy()
            else:
                messagebox.showerror("No se mueve...", "Se ve que algo estoy haciendo mal...")

    # Botón de acceso
        boton_login = tk.Button(emergente3, text="", width=1, bg="darkslategray", font=("Arial", 8), command=validar_credenciales1)
        boton_login.place(x=390, y=545)

    def tv1(self):
        self.sonido_click3.play(1)
        emergente4 = tk.Toplevel(self.ventana)
        emergente4.title("La tv funciona, pero no se logra ver nada")
        emergente4.geometry("800x800")
        emergente4.resizable(False, False)

        # Ruta de la imagen de fondo
        fondo_emergente4_path = os.path.join("img", "tv1.png")
        try:
            fondo_emergente4_img = tk.PhotoImage(file="img/tv1.png") # - - - estaba usando \ y python lo reconoce como otra funcion (carácter de escape)
            fondo_emergente4_label = tk.Label(emergente4, image=fondo_emergente4_img, width=500, height=500)
            fondo_emergente4_label.image = fondo_emergente4_img  # Para evitar que la imagen se elimine por el recolector de basura
            fondo_emergente4_label.place(x=0, y=0, relwidth=1, relheight=1)
        except tk.TclError:
            messagebox.showerror("Error", f"No se pudo cargar la imagen emergente: {fondo_emergente4_path}")


# - - - - C A J O N E R A - - - - #

    def mueble(self):
        self.sonido_click4.play(1)
        emergente4 = tk.Toplevel(self.ventana)
        emergente4.title("Parece que aquí hay información que puede ser de utilidad")
        emergente4.geometry("800x800")
        emergente4.resizable(False, False)

        
        fondo_emergente4_path = os.path.join("img", "mueble.png")
        try:
            fondo_emergente4_img = tk.PhotoImage(file="img/mueble.png")
            fondo_emergente4_label = tk.Label(emergente4, image=fondo_emergente4_img, width=500, height=500)
            fondo_emergente4_label.image = fondo_emergente4_img  
            fondo_emergente4_label.place(x=0, y=0, relwidth=1, relheight=1)
        except tk.TclError:
            messagebox.showerror("Error", f"No se pudo cargar la imagen emergente: {fondo_emergente4_path}")

     
        entry_usuario1 = tk.Entry(emergente4, font=("Arial", 14), width=5, bg="black", fg="green")
        entry_usuario1.place(x=370, y=610)

   
        entry_contraseña1 = tk.Entry(emergente4, font=("Arial", 14), width=5, bg="black", fg="red")
        entry_contraseña1.place(x=370, y=730)

        self.boton7 = tk.Button(emergente4, image=self.imgs[5], compound="top", command=self.cajon,
                                font=("Arial", 12), bg="white", fg="black", width=20, height=20)
        self.boton7.place(x=390, y=490)

    
        def validar_credenciales1():
            usuario = entry_usuario1.get()
            contraseña = entry_contraseña1.get()
            if usuario == "21836" and contraseña == "16948":
                messagebox.showinfo("Parece que el candelabro posee algun tipo de mecanismo...", "Se oye un ruido fuerte, y el mueble se desplaza a un lado...")
                self.pared()
                emergente4.destroy()
            else:
                messagebox.showerror("No se mueve...", "Se ve que algo estoy haciendo mal...")

    # Botón de acceso
        boton_login = tk.Button(emergente4, text="!", bg="black", fg="white", font=("Arial", 6), height=1, width=1, command=validar_credenciales1)
        boton_login.place(x=398, y=385)

# - - - - C A J O N - - - - #

    def cajon(self):
        self.sonido_click4.play(1)
        emergente5 = tk.Toplevel(self.ventana)
        emergente5.title("Veo marcas grabadas al fondo")
        emergente5.geometry("800x800")
        emergente5.resizable(False, False) 

        fondo_emergente5_path = os.path.join("img", "cajon.png")
        try:
            fondo_emergente5_img = tk.PhotoImage(file="img/cajon.png") # - - - estaba usando \ y python lo reconoce como otra funcion (carácter de escape)
            fondo_emergente5_label = tk.Label(emergente5, image=fondo_emergente5_img, width=500, height=500)
            fondo_emergente5_label.image = fondo_emergente5_img  # Para evitar que la imagen se elimine por el recolector de basura
            fondo_emergente5_label.place(x=0, y=0, relwidth=1, relheight=1)
        except tk.TclError:
            messagebox.showerror("Error", f"No se pudo cargar la imagen emergente: {fondo_emergente5_path}")

    def pared(self):
        self.sonido_click5.play(1)
        emergente6 = tk.Toplevel(self.ventana)
        emergente6.title("Aparentemente aquí hay información util")
        emergente6.geometry("800x800")
        emergente6.resizable(False, False) 

        fondo_emergente6_path = os.path.join("img", "pared.png")
        try:
            fondo_emergente6_img = tk.PhotoImage(file="img/pared.png") # - - - estaba usando \ y python lo reconoce como otra funcion (carácter de escape)
            fondo_emergente6_label = tk.Label(emergente6, image=fondo_emergente6_img, width=500, height=500)
            fondo_emergente6_label.image = fondo_emergente6_img  # Para evitar que la imagen se elimine por el recolector de basura
            fondo_emergente6_label.place(x=0, y=0, relwidth=1, relheight=1)
        except tk.TclError:
            messagebox.showerror("Error", f"No se pudo cargar la imagen emergente: {fondo_emergente6_path}")

    def puerta(self):
        self.sonido_click6.play(1)
        emergente7 = tk.Toplevel(self.ventana)
        emergente7.title("Esta puerta esta muy asegurada")
        emergente7.geometry("800x800")
        emergente7.resizable(False, False) 

        fondo_emergente7_path = os.path.join("img", "door.png")
        try:
            fondo_emergente7_img = tk.PhotoImage(file="img/door.png")
            fondo_emergente7_label = tk.Label(emergente7, image=fondo_emergente7_img, width=500, height=500)
            fondo_emergente7_label.image = fondo_emergente7_img  
            fondo_emergente7_label.place(x=0, y=0, relwidth=1, relheight=1)
        except tk.TclError:
            messagebox.showerror("Error", f"No se pudo cargar la imagen emergente: {fondo_emergente7_path}")

        entry_usuario3 = tk.Entry(emergente7, font=("Arial", 14), width=5, bg="black", fg="red")
        entry_usuario3.place(x=265, y=340)

   
        entry_contraseña = tk.Entry(emergente7, font=("Arial", 14), width=5, bg="black", fg="green")
        entry_contraseña.place(x=450, y=310)

        entry_contraseña1 = tk.Entry(emergente7, font=("Arial", 14), width=5, bg="black", fg="blue")
        entry_contraseña1.place(x=585, y=325)


        def validar_credenciales2():
            usuario = entry_usuario3.get()
            contraseña = entry_contraseña.get()
            contraseña2 = entry_contraseña1.get()
            if usuario == "casa" and contraseña == "baja" and contraseña2 =="696":
                messagebox.showinfo("Eh logrado salir...", "...Pero la pesadilla continua")
                """ self.puerta() """
                self.ventana.destroy()
            else:
                messagebox.showerror("No se mueve...", "Se ve que algo estoy haciendo mal...")

    # Botón de acceso
        boton_login1 = tk.Button(emergente7, text="", bg="gray", fg="white", font=("Arial", 6), height=1, width=1, command=validar_credenciales2)
        boton_login1.place(x=750, y=745)

   
    def run(self):
        self.ventana.mainloop()

Juego = Room()
Juego.run()