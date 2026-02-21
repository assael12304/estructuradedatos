# ciclo for
numeros= [3,5,8,9,12]
def sumar_numeros(numeros : list) -> int:
    resultado = 0
    for numero in numeros:
        print(resultado)
        resultado += numero
    return resultado


# ciclo while 
def sumar_numeros_while(numeros:list) -> int:
    resultado=0
    i=0
    while i <len (numeros):
        i +=1
return resultado



    




def sol(numero)-> int:
    if numero == 0 or numero== 1:
        return 1
    while numero > 1:
        
        return numero * sol(numero-1)
   print(sol(8))



def factorial(numero)-> int:
    acumulado = 1
    for i in range(1, numero + 1):
        acumulado *= i
    return acumulado
print(factorial(8))