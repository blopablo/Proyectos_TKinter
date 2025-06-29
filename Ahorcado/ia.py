import tkinter as tk
from random import choice

class Ahorcado:
    def __init__(self):
        self.palabra = choice(
["amor", "avion", "abuelo", "abogado", "arena", "atomo", "amigo", "album", "arte", "animal", "azucar", "arbol", "altura", "aire", "aro", "aceite", "agenda", "anillo", "agua", "ave",
"barco", "barro", "banco", "bebida", "boca", "brisa", "banco", "barril", "bomba", "buque", "buey", "boton", "brazo", "bolsa", "baston", "brillo", "burro", "bateria", "balon", "bingo",
"casa", "coche", "cancion", "ciencia", "cielo", "calor", "camino", "comida", "cuadro", "cuna", "corte", "clase", "clave", "cuento", "color", "copa", "costo", "cesped", "cuento", "circulo",
"dedo", "ducha", "dulce", "dado", "dinero", "dragón", "diario", "deporte", "diente", "doble", "desierto", "dosis", "dulzura", "descanso", "delgado", "domino", "diamante", "disco", "diva", "decada",
"estrella", "espejo", "escalera", "energia", "error", "escuela", "ejemplo", "edificio", "espacio", "etapa", "estrecho", "exito", "embarazo", "encanto", "escultura", "estilo", "emblema", "envoltorio", "esfuerzo", "equipo",
"fuego", "familia", "fabrica", "favor", "felicidad", "fruta", "futuro", "fantasia", "fondo", "factor", "figura", "flor", "frase", "faro", "final", "forma", "fuente", "fila", "firma", "freno",
"gato", "guitarra", "gol", "grande", "gafas", "gente", "gusto", "garaje", "gimnasio", "gallo", "gema", "guardar", "gramo", "giro", "globo", "garfio", "grieta", "galeria", "grano", "guerra",
"huevo", "hombre", "helado", "hogar", "historia", "hora", "hospital", "hierro", "hongo", "hermano", "humor", "habitacion", "hechizo", "honor", "herramienta", "hueso", "huerto", "heroina", "halcon", "humano",
"isla", "iglesia", "imagen", "idea", "incremento", "impacto", "incienso", "instrumento", "indice", "ingrediente", "intento", "invierno", "insecto", "igualdad", "interes", "ilegalidad", "iletrismo", "ilusion", "infinito", "intencion",
"juego", "jabón", "jirafa", "jarron", "jardin", "joya", "junio", "juez", "jarabe", "jabali", "joyeria", "jornada", "jerarquia", "jazmin", "jersey", "juguete", "jornada", "junta", "justicia", "jet",
"karate", "kilo", "kilometro", "kiosco", "kiwi", "karaoke", "kayak", "kebab", "karma", "kimono", "kayak", "krypton", "kalimba", "kamikaze", "koala", "krypton", "kodak", "kit", "kermes", "kilos",
"luz", "libro", "lago", "lengua", "lente", "lado", "leccion", "libertad", "llave", "labor", "luz", "leche", "larga", "luna", "llama", "lenguaje", "leyenda", "locura", "lujo", "lectura",
"mundo", "mano", "mar", "madera", "mujer", "musica", "mapa", "mes", "moneda", "medicina", "mensaje", "momento", "modelo", "memoria", "montana", "miedo", "mujer", "marca", "metal", "magia",
"noche", "niño", "nombre", "nube", "nariz", "nota", "numero", "necesidad", "naturaleza", "nuevo", "negocio", "navidad", "niña", "narciso", "navio", "noticia", "normal", "nota", "naranja", "nivel",
"ojo", "olor", "ocasión", "obra", "origen", "ojo", "oasis", "octubre", "oficina", "olla", "otro", "onda", "opcion", "onda", "oportunidad", "organismo", "oxigeno", "oscuro", "orden", "oido",
"padre", "puerta", "pueblo", "perro", "poner", "paz", "palabra", "pieza", "pintura", "persona", "peso", "pluma", "planeta", "polvo", "prisma", "precio", "programa", "proyecto", "pasion", "profesor",
"queso", "quebracho", "quimica", "quinto", "quitar", "quimono", "quince", "quasar", "quita", "quieto", "queja", "quimico", "quimera", "quiosco", "quorum", "quimono", "quedar", "querer", "quillon", "quirurgico",
"raton", "rosa", "ruido", "raton", "rojo", "reloj", "risa", "ruby", "radio", "recuerdo", "retorno", "reino", "riera", "rango", "rapido", "rueda", "reina", "raiz", "ritmo", "rugido",
"sol", "silla", "sueño", "sabor", "salud", "sombra", "sistema", "suerte", "silla", "silencio", "sangre", "sabor", "soldado", "sentido", "sabana", "sello", "suelo", "sequía", "sesion", "silaba",
"tierra", "telefono", "tiempo", "tren", "teatro", "taza", "tacto", "tiempo", "tanque", "tigre", "texto", "tarea", "tema", "techo", "tabla", "tumba", "tecla", "tecnologia", "tropa", "trabajo",
"universo", "unidad", "ultimo", "unico", "uso", "utilidad", "udas", "urbanidad", "uvas", "universidad", "urgencia", "urna", "usuario", "utopia", "uro", "ultrasonido", "util", "usura", "ultimo", "usor",
"viento", "ventana", "valor", "vuelo", "verdad", "vista", "voz", "version", "vaca", "vaso", "viaje", "video", "vertical", "vecino", "vocal", "velocidad", "vacuna", "velero", "verano", "vampiro",
"whisky", "wifi", "wafle", "web", "walkie", "waterpolo", "windsurf", "western", "wasabi", "wolframio", "wolverine", "wifi", "webinar", "whatsapp", "woofer", "workshop", "wagon", "waldo", "wafer", "wise",
"xilofono", "xenon", "xilografia", "xenofobia", "xerófito", "xenón", "xenial", "xifoides", "xantina", "xerografia", "xenogenesis", "xerofilo", "xantofila", "xilografía", "xenomas", "xerófago", "xilófono", "xifias", "xenón", "xantoma",
"yate", "yogur", "yema", "yerba", "yunque", "yacer", "yarda", "yogui", "yocto", "yodo", "yegua", "yacimiento", "yaqui", "yema", "yugo", "yeguarizo", "yate", "yema", "yodo", "yogurt",
"zapato", "zorro", "zumo", "zafiro", "zona", "zanco", "zarza", "zanahoria", "zanja", "zigzag", "zodíaco", "zumba", "zoologico", "zoologo", "zoquete", "zafarse", "zas", "zarpar", "zarcillo", "zombi"])
        self.adivinada = ["_"] * len(self.palabra)
        self.intentos = 6

        self.ventana = tk.Tk()
        self.ventana.title("Ahorcado")
        self.ventana.geometry("600x600")  # Asegura un tamaño consistente

        self.portada = tk.Label(self.ventana, text="AHO__ADO", font=("Arial", 30), bg="black", fg="DARKSEAGREEN4")
        self.portada.place(x=10, y=15)

        # Cargar imagen de fondo
        self.fondo = tk.PhotoImage(file="img\Ahorcado.png")  
        self.canvas = tk.Canvas(self.ventana, width=600, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.fondo, anchor="nw")

        # Widgets sobre el fondo
        self.etiqueta_palabra = tk.Label(self.ventana, text=" ".join(self.adivinada), font=("Arial", 24), bg="#ffffff")
        self.etiqueta_intentos = tk.Label(self.ventana, text=f"Intentos: {self.intentos}", font=("Arial", 18), bg="#ffffff")
        self.campo_letra = tk.Entry(self.ventana, font=("Arial", 18))
        self.boton_adivinar = tk.Button(self.ventana, text="A D I V I N A R", command=self.adivinar)

        # Posicionar widgets en el Canvas
        self.canvas.create_window(300, 80, window=self.etiqueta_palabra)
        self.canvas.create_window(300, 150, window=self.etiqueta_intentos)
        self.canvas.create_window(300, 220, window=self.campo_letra)
        self.canvas.create_window(300, 290, window=self.boton_adivinar)

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