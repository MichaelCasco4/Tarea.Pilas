class Documento:
    def __init__(self, Nombre, Cuerpo):
        self.Nombre = Nombre
        self.Cuerpo = Cuerpo

    def __str__(self):
        return "Título:" +  self.Nombre + " " + "Cuerpo:" + self.Cuerpo
