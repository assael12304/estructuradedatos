class Nodo:
    def __init__(self, vehiculo):
        self.vehiculo = vehiculo  # guarda el vehiculo
        self.siguiente = None     # apunta al siguiente nodo, al inicio no hay ninguno


class ColasVehiculo:
    def __init__(self):
        self.frente = None  # primer nodo
        self.final = None   # ultimo nodo

    def agregar(self, vehiculo):
        nodo = Nodo(vehiculo)
        if self.final is None:
            self.frente = nodo
            self.final = nodo
        else:
            self.final.siguiente = nodo
            self.final = nodo
        print(f"Agregado: {vehiculo['tipo']} {vehiculo['marca']} {vehiculo['modelo']}")

    def despachar(self):
        if self.frente is None:
            print("La cola esta vacia")
            return
        vehiculo = self.frente.vehiculo
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        print(f"Despachado: {vehiculo['tipo']} {vehiculo['marca']} {vehiculo['modelo']}")

    def mostrar(self):
        if self.frente is None:
            print("La cola esta vacia")
            return
        nodo_actual = self.frente
        numero = 1
        print("--- Cola ---")
        while nodo_actual is not None:
            v = nodo_actual.vehiculo
            print(f"{numero}. {v['tipo']} {v['marca']} {v['modelo']} {v['anio']}")
            nodo_actual = nodo_actual.siguiente
            numero += 1
        print("------------")


# ---------- Prueba ----------
cola = ColasVehiculo()

cola.agregar({"tipo": "Motocicleta", "marca": "Honda", "modelo": "CB500", "anio": 2020})
cola.agregar({"tipo": "Automovil",   "marca": "Toyota", "modelo": "Corolla", "anio": 2019})
cola.agregar({"tipo": "Motocicleta", "marca": "Yamaha", "modelo": "R3", "anio": 2022})

cola.mostrar()
cola.despachar()
cola.mostrar()