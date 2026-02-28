# ── ciclo WHILE ──────────────────────────────────────────
def hanoi_w(n, origen, destino, auxiliar):
    movimientos = 0
    i = 1
    while i <= n:
        print(f"Mover disco {i} de {origen} a {destino}")
        movimientos += 1
        i += 1
    print(f"Total movimientos: {movimientos}\n")

hanoi_w(3, "A", "C", "B")


#  ciclo FOR 
def hanoi_f(n, origen, destino, auxiliar):
    movimientos = 0
    for i in range(1, n + 1):
        print(f"Mover disco {i} de {origen} a {destino}")
        movimientos += 1
    print(f"Total movimientos: {movimientos}\n")

hanoi_f(3, "A", "C", "B")


#  RECURSIVA 
def hanoi_r(n, origen, destino, auxiliar):
    # caso base: si no hay discos, no hacemos nada
    if n == 0:
        return

    # paso 1: mover los discos de arriba al auxiliar
    hanoi_r(n - 1, origen, auxiliar, destino)

    # paso 2: mover el disco grande al destino
    print(f"Mover disco {n} de {origen} a {destino}")

    # paso 3: mover los discos del auxiliar al destino
    hanoi_r(n - 1, auxiliar, destino, origen)

hanoi_r(3, "A", "C", "B")



