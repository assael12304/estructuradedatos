# while
def busqueda_binaria_while(arr, objetivo):
    izq = 0
    der = len(arr) - 1
    
    while izq <= der:
        medio = (izq + der) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif objetivo < arr[medio]:
            der = medio - 1
        else:
            izq = medio + 1
    
    return -1

print (busqueda_binaria_while([1,2,3,4,5,6,7,8,9],9))


#for
def busqueda_binaria_for(arr, objetivo):
    izq = 0
    der = len(arr) - 1
    
    for _ in range(len(arr)):
        if izq > der:
            return -1
            
        medio = (izq + der) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif objetivo < arr[medio]:
            der = medio - 1
        else:
            izq = medio + 1
    
    return -1

print(busqueda_binaria_for([1,2,3,4,5,6,7,8,9],5))


#recursiva
def busqueda_binaria_recursiva(arr, objetivo):
    return busqueda_binaria(arr, objetivo, 0, len(arr) - 1)


def busqueda_binaria(arr, objetivo, izq, der):
    if izq > der:
        return -1
    
    medio = (izq + der) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif objetivo < arr[medio]:
        return busqueda_binaria(arr, objetivo, izq, medio - 1)
    else:
        return busqueda_binaria(arr, objetivo, medio + 1, der)


arr = [1,2,3,4,5,6,7,8,9]
print(busqueda_binaria_recursiva(arr, 6))