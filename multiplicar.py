#  ciclo WHILE
def multiplicar_w(a, b):
    resultado = 0
    i = 0
    while i < b:
        resultado = resultado + a   # sumamos 'a', 'b' veces
        i = i + 1
    return resultado

print(multiplicar_w(4, 3))   # 12
print(multiplicar_w(7, 0))   # 0
print(multiplicar_w(0, 9))   # 0
print(multiplicar_w(6, 6))   # 36


#  FOR 
def multiplicar_f(a, b):
    resultado = 0
    for i in range(b):
        resultado = resultado + a   # sumamos 'a', 'b' veces
    return resultado

print(multiplicar_f(4, 3))   # 12
print(multiplicar_f(7, 0))   # 0
print(multiplicar_f(0, 9))   # 0
print(multiplicar_f(6, 6))   # 36


# RECURSIVA 
def multiplicar_r(a, b):
    # caso base: si b es 0, el resultado es 0
    if b == 0:
        return 0

    # caso recursivo: sumamos 'a' una vez y llamamos con b-1
    return a + multiplicar_r(a, b - 1)

print(multiplicar_r(4, 3))   # 12
print(multiplicar_r(7, 0))   # 0
print(multiplicar_r(0, 9))   # 0
print(multiplicar_r(6, 6))   # 36