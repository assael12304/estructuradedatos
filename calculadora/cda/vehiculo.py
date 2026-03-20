class Vehiculo:
    def __init__(self, marca, modelo, anio, tipo):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.tipo = tipo

class Motocicleta:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.tipo = "Motocicleta"

class Automovil:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.tipo = "Automovil"

class Nodo:
    def __init__(self, vehiculo):
        self.vehiculo = vehiculo
        self.siguiente = None

class ColasVehiculo:
    def __init__(self):
        self.frente = None
        self.final = None

    def agregar_vehiculo(self, marca, modelo, anio, tipo):
        if tipo == "Motocicleta":
            vehiculo = Motocicleta(marca, modelo, anio)
        elif tipo == "Automovil":
            vehiculo = Automovil(marca, modelo, anio)
        else:
            print("Tipo no valido")
            return

        nodo = Nodo(vehiculo)

        if self.final is None:
            self.frente = nodo
            self.final = nodo
        else:
            self.final.siguiente = nodo
            self.final = nodo

        print(f"Agregado: {vehiculo.tipo} {vehiculo.marca} {vehiculo.modelo} {vehiculo.anio}")

    def despachar_vehiculo(self):
        if self.frente is None:
            print("La cola esta vacia")
            return

        vehiculo = self.frente.vehiculo
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.final = None

        print(f"Despachado: {vehiculo.tipo} {vehiculo.marca} {vehiculo.modelo} {vehiculo.anio}")

    def mostrar_vehiculos(self):
        if self.frente is None:
            print("La cola esta vacia")
            return

        nodo_actual = self.frente
        numero = 1
        print("--- Cola de vehiculos ---")
        while nodo_actual is not None:
            v = nodo_actual.vehiculo
            print(f"{numero}. {v.tipo} {v.marca} {v.modelo} {v.anio}")
            nodo_actual = nodo_actual.siguiente
            numero += 1
        print("-------------------------")


# ---------- Prueba ----------
cola = ColasVehiculo()

cola.agregar_vehiculo("Honda", "CB500", 2020, "Motocicleta")
cola.agregar_vehiculo("Toyota", "Corolla", 2019, "Automovil")
cola.agregar_vehiculo("Yamaha", "R3", 2022, "Motocicleta")

cola.mostrar_vehiculos()

cola.despachar_vehiculo()

cola.mostrar_vehiculos()
