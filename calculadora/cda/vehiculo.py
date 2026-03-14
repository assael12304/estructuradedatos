class vehiculo:
    def __init__(self, marca: str, modelo: str, anio:int,tipo: str):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio 
    def mostrar_informacion(self):
        return f"{self.marca} {self.modelo} ({self.anio})"