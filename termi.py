# ciclo while
def sol(numero)-> int:
    if numero == 0 or numero== 1:
        return 1
    while numero > 1:
        
        return numero * sol(numero-1)
print(sol(9))

#ciclo for

def factorial(numero)-> int:
    acumulado = 1
    for i in range(1, numero + 1):
        acumulado *= i
    return acumulado
print(factorial(7))


# recursividad

def factorial_recursivo(numero)-> int:
    if numero == 0 or numero== 1:
        return 1
    else:
        return numero * factorial_recursivo(numero - 1)
    
print(factorial_recursivo(7))