# ciclo for
# CICLO FOR - Suma de números
numeros = [3, 5, 8, 9, 12]

def sumar_numeros(numeros: list) -> int:
    resultado = 0
    for numero in numeros:
        print(resultado)        # Muestra el resultado antes de sumar
        resultado += numero     # Acumula la suma
    return resultado

print(sumar_numeros(numeros))   


#  CICLO WHILE  Suma de números 
def sumar_numeros_while(numeros: list) -> int:
    resultado = 0
    i = 0
    while i < len(numeros):
        resultado += numeros[i]  
        i += 1                   
    return resultado             

print(sumar_numeros_while(numeros))  


#  FACTORIAL RECURSIVO 
def sol(numero) -> int:
    if numero == 0 or numero == 1:  
        return 1
    if numero > 1:                  
        return numero * sol(numero - 1)

print(sol(8))                       


#  FACTORIAL CON FOR 
def factorial(numero) -> int:
    acumulado = 1
    for i in range(1, numero + 1):
        acumulado *= i
    return acumulado

print(factorial(8))