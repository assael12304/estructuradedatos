class Motocicleta:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.tipo = "Motocicleta"

# ---------- Prueba ----------
m = Motocicleta("Honda", "CB500", 2020)
print(m.tipo, m.marca, m.modelo, m.anio)